"""Load and persist user-defined settings for Obsidian vault export in JSON format."""

import json
from dataclasses import asdict
from pathlib import Path

from obsidian_to_txt.models import Settings


class SettingsLoadError(Exception):
    """Raised when settings cannot be loaded or validated."""


class SettingsSaveError(Exception):
    """Raised when settings cannot be saved."""


SETTINGS_PATH = Path(".config") / "obsidian-to-txt" / "settings.json"


def load_settings() -> Settings | None:
    """Load settings from JSON."""
    if not SETTINGS_PATH.exists():
        return None

    try:
        raw = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SettingsLoadError(f"Failed to load settings from {SETTINGS_PATH}: {exc}") from exc

    return Settings(
        vault_path=Path(raw["vault_path"]),
        output_path=Path(raw["output_path"]),
        ignore_directories=set(raw["ignore_directories"]),
        ignore_files=set(raw["ignore_files"]),
    )


def save_settings(settings: Settings) -> None:
    """Save settings to JSON."""
    payload = asdict(settings)

    payload["vault_path"] = str(settings.vault_path)
    payload["output_path"] = str(settings.output_path)
    payload["ignore_directories"] = sorted(settings.ignore_directories)
    payload["ignore_files"] = sorted(settings.ignore_files)

    try:
        SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
        SETTINGS_PATH.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except OSError as exc:
        raise SettingsSaveError(f"Failed to save settings to {SETTINGS_PATH}: {exc}") from exc
