import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
APP_ENV = os.getenv("APP_ENV", "dev")
APP_SECRET = os.getenv("APP_SECRET", "change_me")
DATABASE_URL = os.getenv("DATABASE_URL")


ENTRA_TENANT_ID = os.getenv("ENTRA_TENANT_ID")
ENTRA_CLIENT_ID = os.getenv("ENTRA_CLIENT_ID")
ENTRA_CLIENT_SECRET = os.getenv("ENTRA_CLIENT_SECRET")
ENTRA_API_AUDIENCE = os.getenv("ENTRA_API_AUDIENCE")


GRAPH_BASE = os.getenv("GRAPH_BASE", "https://graph.microsoft.com/v1.0")
GRAPH_DEFAULT_ORG_CALENDAR = os.getenv("GRAPH_DEFAULT_ORG_CALENDAR")


GLPI_BASE_URL = os.getenv("GLPI_BASE_URL")
GLPI_APP_TOKEN = os.getenv("GLPI_APP_TOKEN")
GLPI_USER_TOKEN = os.getenv("GLPI_USER_TOKEN")


KB_ROOT = os.getenv("KB_ROOT", "/mnt/interventions/kb")
SHEETS_ROOT = os.getenv("SHEETS_ROOT", "/mnt/interventions/sheets")


settings = Settings()