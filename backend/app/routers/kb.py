from fastapi import APIRouter, Depends
from ..deps import get_current_user
from ..services.storage import list_kb


router = APIRouter(prefix="/kb", tags=["knowledge-base"])


@router.get("/")
async def get_kb(user=Depends(get_current_user)):
return {"files": list_kb()}