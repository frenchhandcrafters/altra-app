from fastapi import FastAPI
from .db import Base, engine
from .routers import interventions, kb, tickets


# Create tables (dev). For prod, use Alembic.
Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
app = FastAPI(title="Altra Interventions API")
app.include_router(interventions.router)
app.include_router(kb.router)
app.include_router(tickets.router)
return app