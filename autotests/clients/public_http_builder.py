from clients.event_hooks import curl_event_hook
from httpx import Client

def get_public_http_client() -> Client:
    return Client(timeout=100, base_url="http://localhost:8000", event_hooks={"request": [curl_event_hook]})