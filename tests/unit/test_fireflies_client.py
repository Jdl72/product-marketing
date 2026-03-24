import io
import json
import unittest
from unittest.mock import MagicMock, patch
import urllib.error
import warnings

from tests.test_helpers import load_module


client_module = load_module("fireflies_client", "connectors/fireflies/client.py")

warnings.filterwarnings(
    "ignore",
    category=ResourceWarning,
    message=r"Implicitly cleaning up <HTTPError .*",
)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def read(self):
        return json.dumps(self.payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class FakeHTTPError(urllib.error.HTTPError):
    def __init__(self, url, code, msg, body):
        super().__init__(url, code, msg, hdrs=None, fp=None)
        self._body = body

    def read(self):
        return self._body


class FirefliesClientUnitTests(unittest.TestCase):
    def test_requires_api_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                client_module.FirefliesClient()

    @patch.object(client_module.certifi, "where", return_value="/tmp/cacert.pem")
    @patch.object(client_module.ssl, "create_default_context")
    @patch.object(client_module.urllib.request, "urlopen")
    def test_query_returns_data_payload(self, mock_urlopen, mock_context, _mock_certifi):
        mock_context.return_value = object()
        mock_urlopen.return_value = FakeResponse({"data": {"transcripts": [{"id": "abc"}]}})
        client = client_module.FirefliesClient(api_key="test-key")

        data = client.query("query { transcripts { id } }", {"limit": 1})

        self.assertEqual(data, {"transcripts": [{"id": "abc"}]})
        request = mock_urlopen.call_args.args[0]
        self.assertEqual(request.get_header("Authorization"), "Bearer test-key")

    @patch.object(client_module.certifi, "where", return_value="/tmp/cacert.pem")
    @patch.object(client_module.ssl, "create_default_context")
    @patch.object(client_module.urllib.request, "urlopen")
    def test_query_raises_runtime_error_for_http_errors(self, mock_urlopen, mock_context, _mock_certifi):
        mock_context.return_value = object()
        http_error = FakeHTTPError(
            client_module.API_URL,
            400,
            "Bad Request",
            b'{"error":"bad"}',
        )
        mock_urlopen.side_effect = http_error
        client = client_module.FirefliesClient(api_key="test-key")

        with self.assertRaises(RuntimeError) as context:
            client.query("query { bad }")

        self.assertIn("Fireflies API error: 400", str(context.exception))

    @patch.object(client_module.FirefliesClient, "query")
    def test_list_and_get_transcript_call_query_with_expected_variables(self, mock_query):
        mock_query.side_effect = [
            {"transcripts": [{"id": "one"}]},
            {"transcript": {"id": "two"}},
        ]
        client = client_module.FirefliesClient(api_key="test-key")

        transcripts = client.list_transcripts(limit=3)
        transcript = client.get_transcript("transcript-123")

        self.assertEqual(transcripts, [{"id": "one"}])
        self.assertEqual(transcript, {"id": "two"})
        self.assertEqual(mock_query.call_args_list[0].args[1], {"limit": 3})
        self.assertEqual(mock_query.call_args_list[1].args[1], {"transcriptId": "transcript-123"})


if __name__ == "__main__":
    unittest.main()
