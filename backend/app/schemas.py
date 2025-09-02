from pydantic import BaseModel, EmailStr
from datetime import datetime


class InterventionCreate(BaseModel):
title: str
description: str | None = None
client_id: int
technician_id: int
start_at: datetime
end_at: datetime


class InterventionOut(BaseModel):
id: int
title: str
description: str | None
start_at: datetime
end_at: datetime
status: str


class Config:
from_attributes = True