#!/usr/bin/env python3
"""Fetch a LinkedIn job posting via BrightData API."""

import sys
import json
import time
import urllib.request
import os

API_KEY = os.environ.get("BRIGHTDATA_API_KEY", "")
DATASET_ID = "gd_lpfll7v5hcqtkxl6l"
TRIGGER_URL = f"https://api.brightdata.com/datasets/v3/trigger?dataset_id={DATASET_ID}&format=json"
SNAPSHOT_BASE = "https://api.brightdata.com/datasets/v3/snapshot"


def trigger(url):
    payload = json.dumps([{"url": url}]).encode()
    req = urllib.request.Request(
        TRIGGER_URL,
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
    if len(sys.argv) < 2:
        print("Usage: fetch_linkedin_job.py <linkedin-job-url-or-id>", file=sys.stderr)
        sys.exit(1)

    arg = sys.argv[1]
    url = arg if arg.startswith("http") else f"https://www.linkedin.com/jobs/view/{arg}"

    print(f"Fetching: {url}", file=sys.stderr)
    snapshot_id = trigger(url)
    print(f"Snapshot {snapshot_id} — polling every 5s...", file=sys.stderr)
    jobs = poll(snapshot_id)

    result = jobs[0] if len(jobs) == 1 else jobs
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
