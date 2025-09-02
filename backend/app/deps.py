from fastapi import Depends, HTTPException, status, Header


# Minimal placeholder: accept an internal token for first run.
# Replace with Entra (OIDC) validation shortly.


def get_current_user(authorization: str | None = Header(default=None)):
if not authorization or authorization != "Bearer DEV":
raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
return {"id": 1, "role": "admin", "name": "Dev User"}