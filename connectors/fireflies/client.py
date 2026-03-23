import json
import os
import ssl
import urllib.error
import urllib.request

import certifi


API_URL = "https://api.fireflies.ai/graphql"


class FirefliesClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("FIREFLIES_API_KEY")
        if not self.api_key:
            raise ValueError("FIREFLIES_API_KEY is required")

    def query(self, query, variables=None):
        payload = {"query": query, "variables": variables or {}}
        request = urllib.request.Request(
            API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        try:
            with urllib.request.urlopen(request, context=ssl_context) as response:
                body = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Fireflies API error: {exc.code} {detail}") from exc
        data = json.loads(body)
        if data.get("errors"):
            raise RuntimeError(f"Fireflies GraphQL errors: {data['errors']}")
        return data.get("data", {})

    def list_transcripts(self, limit=10):
        query = """
        query($limit: Int) {
          transcripts(limit: $limit) {
            id
            title
            date
            duration
            organizer_email
          }
        }
        """
        data = self.query(query, {"limit": limit})
        return data.get("transcripts", [])

    def get_transcript(self, transcript_id):
        query = """
        query($transcriptId: String!) {
          transcript(id: $transcriptId) {
            id
            title
            date
            duration
            organizer_email
            participants
            sentences {
              index
              speaker_name
              speaker_id
              text
              start_time
              end_time
            }
          }
        }
        """
        data = self.query(query, {"transcriptId": transcript_id})
        return data.get("transcript")
