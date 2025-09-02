import httpx
from ..config import settings


async def create_ticket(title: str, content: str, requester_email: str | None = None):
headers = {
"App-Token": settings.GLPI_APP_TOKEN,
"Authorization": f"user_token {settings.GLPI_USER_TOKEN}",
"Content-Type": "application/json",
}
payload = {
"input": {
"name": title,
"content": content,
"_users_id_requester": 0,
"_users_id_requester_notif": 1,
"_users_id_recipient": 0,
}
}
async with httpx.AsyncClient(timeout=20) as client:
r = await client.post(f"{settings.GLPI_BASE_URL}/Ticket", json=payload, headers=headers)
r.raise_for_status()
return r.json()