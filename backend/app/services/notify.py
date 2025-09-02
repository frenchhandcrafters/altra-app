from ..services.graph_token import get_app_token
from ..config import settings
import httpx


async def send_email(to_email: str, subject: str, html: str):
token = await get_app_token()
url = f"{settings.GRAPH_BASE}/users/{settings.GRAPH_DEFAULT_ORG_CALENDAR}/sendMail"
msg = {
"message": {
"subject": subject,
"body": {"contentType": "HTML", "content": html},
"toRecipients": [{"emailAddress": {"address": to_email}}],
}
}
async with httpx.AsyncClient(timeout=20) as client:
r = await client.post(url, json=msg, headers={"Authorization": f"Bearer {token}"})
r.raise_for_status()