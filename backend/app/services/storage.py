from pathlib import Path
from ..config import settings


KB_ROOT = Path(settings.KB_ROOT)
SHEETS_ROOT = Path(settings.SHEETS_ROOT)


KB_ROOT.mkdir(parents=True, exist_ok=True)
SHEETS_ROOT.mkdir(parents=True, exist_ok=True)


def list_kb():
return [str(p.relative_to(KB_ROOT)) for p in KB_ROOT.rglob('*') if p.is_file()]