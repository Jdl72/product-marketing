#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from connectors.fireflies.client import FirefliesClient


def main():
    parser = argparse.ArgumentParser(description="Fetch transcripts from Fireflies")
    parser.add_argument("--limit", type=int, default=10, help="Number of transcripts to list")
    parser.add_argument("--transcript-id", help="Fetch one transcript by ID")
    parser.add_argument(
        "--output",
        help="Optional output path for JSON",
    )
    args = parser.parse_args()

    client = FirefliesClient()

    if args.transcript_id:
        payload = client.get_transcript(args.transcript_id)
    else:
        payload = client.list_transcripts(limit=args.limit)

    text = json.dumps(payload, indent=2)
    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
