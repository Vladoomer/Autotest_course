from clients.event_hooks import curl_event_hook
from httpx import Client
from config import settings

def get_public_http_client() -> Client:
    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        event_hooks={"request": [curl_event_hook]})