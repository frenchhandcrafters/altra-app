import httpx
from . import graph_token
from ..config import settings


# NOTE: choose one model:
# 1) Application permissions (admin-consented) => app-only token writes to any user calendar
# 2) Delegated OBO flow => create event in the signed-in technician calendar


async def create_event_for_user(upn: str, subject: str, body: str, start_iso: str, end_iso: str) -> str:
token = await graph_token.get_app_token()
url = f"{settings.GRAPH_BASE}/users/{upn}/events"
payload = {
"subject": subject,
"body": {"contentType": "HTML", "content": body or ""},
"start": {"dateTime": start_iso, "timeZone": "Europe/Paris"},
"end": {"dateTime": end_iso, "timeZone": "Europe/Paris"},
"showAs": "busy",
"isReminderOn": True,
}
async with httpx.AsyncClient(timeout=20) as client:
r = await client.post(url, json=payload, headers={"Authorization": f"Bearer {token}"})
r.raise_for_status()
return r.json().get("id")