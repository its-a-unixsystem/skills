#!/usr/bin/env python3
"""Search LinkedIn jobs via BrightData Datasets API."""

import sys
import json
import time
import urllib.request
import argparse
import os

API_KEY = os.environ.get("BRIGHTDATA_API_KEY", "")
DATASET_ID = "gd_lpfll7v5hcqtkxl6l"
TRIGGER_BASE = (
    f"https://api.brightdata.com/datasets/v3/trigger"
    f"?dataset_id={DATASET_ID}&format=json&type=discover_new&discover_by=keyword"
)
SNAPSHOT_BASE = "https://api.brightdata.com/datasets/v3/snapshot"


DEFAULT_LIMIT = 25


def trigger(filters, limit):
    url = f"{TRIGGER_BASE}&limit_per_input={limit}"
    payload = json.dumps([filters]).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())["snapshot_id"]


def poll(snapshot_id):
    url = f"{SNAPSHOT_BASE}/{snapshot_id}?format=json"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {API_KEY}"})
    while True:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read())
        if isinstance(data, list):
            return data
        if data.get("status") == "running":
            time.sleep(5)
            continue
        raise RuntimeError(f"Unexpected response: {data}")


def main():
    parser = argparse.ArgumentParser(description="Search LinkedIn jobs via BrightData")
    parser.add_argument("keyword", help="Job title or keywords")
    parser.add_argument("--location", required=True, help="Location (e.g. 'United States', 'San Francisco, CA')")
    parser.add_argument("--remote", choices=["Remote", "On-site", "Hybrid"])
    parser.add_argument(
        "--time-range", dest="time_range",
        choices=["Past 24 hours", "Past week", "Past month"],
        default="Past month",
    )
    parser.add_argument(
        "--job-type", dest="job_type",
        choices=["Full-time", "Part-time", "Contract", "Temporary", "Volunteer"],
    )
    parser.add_argument(
        "--experience",
        choices=["Entry level", "Associate", "Mid-Senior level", "Director", "Executive", "Internship"],
    )
    parser.add_argument("--company", help="Filter by company name")
    parser.add_argument("--country", help="Country code (e.g. US, GB, FR)")
    parser.add_argument(
        "--limit", type=int, default=DEFAULT_LIMIT,
        help=f"Max results (default {DEFAULT_LIMIT})",
    )
    args = parser.parse_args()

    filters = {"keyword": args.keyword, "location": args.location}
    if args.remote:
        filters["remote"] = args.remote
    if args.time_range:
        filters["time_range"] = args.time_range
    if args.job_type:
        filters["job_type"] = args.job_type
    if args.experience:
        filters["experience_level"] = args.experience
    if args.company:
        filters["company"] = args.company
    if args.country:
        filters["country"] = args.country

    print(f"Searching (limit {args.limit}): {filters}", file=sys.stderr)
    snapshot_id = trigger(filters, args.limit)
    print(f"Snapshot {snapshot_id} — polling every 5s...", file=sys.stderr)
    jobs = poll(snapshot_id)
    print(json.dumps(jobs, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
