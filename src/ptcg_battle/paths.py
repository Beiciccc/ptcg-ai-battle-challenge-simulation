from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw" / "competition"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
SUBMISSIONS_DIR = ARTIFACTS_DIR / "submissions"
SUBMISSION_SOURCE_DIR = PROJECT_ROOT / "submission"

EN_CARD_DATA = RAW_DATA_DIR / "EN_Card_Data.csv"
JP_CARD_DATA = RAW_DATA_DIR / "JP_Card_Data.csv"
