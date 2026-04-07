"""CLI command for first-time interactive settings setup."""

from obsidian_to_txt.settings_store import SETTINGS_PATH, SettingsSaveError, save_settings
from obsidian_to_txt.ui.prompts import prompt_for_settings
from obsidian_to_txt.ui.rich import error, info, settings_preview, success, title


def main() -> None:
    """Run initial setup and persist settings."""
    title("Obsidian to Text: Setup")

    if SETTINGS_PATH.exists():
        info(f"Settings file already exists: {SETTINGS_PATH}")
        info("Use `uv run reset` to update it.")

        return

    try:
        settings = prompt_for_settings()

        settings.ignore_files.add(settings.output_path.name)

        settings_preview(
            settings.vault_path,
            settings.output_path,
            settings.ignore_directories,
            settings.ignore_files,
        )

        save_settings(settings)

        success(f"Settings file saved to: {SETTINGS_PATH}")
    except SettingsSaveError as exc:
        error(f"Setup error: {exc}")

        raise SystemExit(1) from exc
    except (KeyboardInterrupt, EOFError):
        info("Settings file setup cancelled")

        raise SystemExit(130) from None
