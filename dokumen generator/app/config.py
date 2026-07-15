"""
config.py — Loader untuk config.yml dan .env
"""
import os
from pathlib import Path
import yaml
from dotenv import load_dotenv

GENERATOR_DIR = Path(__file__).parent.parent
REPO_ROOT = GENERATOR_DIR.parent
CONFIG_PATH = GENERATOR_DIR / "config.yml"
ENV_PATH = GENERATOR_DIR / ".env"

load_dotenv(ENV_PATH)


def load_config() -> dict:
    """Load config.yml dan merge dengan .env untuk data sensitif."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # Inject data sensitif dari .env ke dalam config
    cfg["company"]["npwp"] = os.getenv("COMPANY_NPWP", "—")
    cfg["company"]["bank"] = os.getenv("COMPANY_BANK", "—")
    cfg["company"]["account_number"] = os.getenv("COMPANY_ACCOUNT_NUMBER", "—")
    cfg["company"]["account_name"] = os.getenv("COMPANY_ACCOUNT_NAME", cfg["company"]["name"])
    cfg["company"]["signatory_name"] = os.getenv("COMPANY_SIGNATORY_NAME", "Aris Winandi")
    cfg["company"]["signatory_title"] = os.getenv("COMPANY_SIGNATORY_TITLE", "Direktur")

    return cfg


# Singleton config agar tidak reload berkali-kali
_config: dict | None = None


def get_config() -> dict:
    global _config
    if _config is None:
        _config = load_config()
    return _config
