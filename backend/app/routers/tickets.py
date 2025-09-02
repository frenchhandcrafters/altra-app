from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import SessionLocal
from .. import models, schemas
from ..deps import get_current_user
from ..services.graph import create_event_for_user
from ..services.notify import send_email


router = APIRouter(prefix="/interventions", tags=["interventions"])


def get_db():
db = SessionLocal()
try:
yield db
finally:
db.close()


@router.post("/", response_model=schemas.InterventionOut)
async def create_intervention(payload: schemas.InterventionCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
tech = db.get(models.Technician, payload.technician_id)
cli = db.get(models.Client, payload.client_id)
if not tech or not cli:
raise HTTPException(status_code=404, detail="Technician or client not found")


iv = models.Intervention(
title=payload.title,
description=payload.description,
client_id=payload.client_id,
technician_id=payload.technician_id,
start_at=payload.start_at,
end_at=payload.end_at,
)
db.add(iv)
db.commit()
db.refresh(iv)


# Create Graph event
event_id = await create_event_for_user(
tech.calendar_upn,
subject=iv.title,
body=iv.description or "",
start_iso=iv.start_at.isoformat(),
end_iso=iv.end_at.isoformat(),
)
iv.graph_event_id = event_id
db.commit()


# Notify client (optional)
if cli.email:
await send_email(cli.email, f"Intervention planifiée: {iv.title}", f"Bonjour, votre intervention est prévue le {iv.start_at}.")


return iv