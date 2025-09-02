import httpx, os
from ..config import settings


# Client Credentials flow for app-only Graph token
async def get_app_token() -> str:
tenant = settings.ENTRA_TENANT_ID
client_id = settings.ENTRA_CLIENT_ID
secret = settings.ENTRA_CLIENT_SECRET
scope = "https://graph.microsoft.com/.default"
url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
data = {
"client_id": client_id,
"client_secret": secret,
"grant_type": "client_credentials",
"scope": scope,
}
async with httpx.AsyncClient(timeout=20) as client:
r = await client.post(url, data=data)
r.raise_for_status()
return r.json()["access_token"]