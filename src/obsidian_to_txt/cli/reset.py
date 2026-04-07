"""CLI command for interactively updating existing settings."""

from obsidian_to_txt.settings_store import (
    SettingsLoadError,
    SettingsSaveError,
    load_settings,
    save_settings,
)
from obsidian_to_txt.ui.prompts import prompt_for_settings
from obsidian_to_txt.ui.rich import error, info, success, title


def main() -> None:
    """Reset the settings file from interactive prompts."""
    title("Obsidian to Text: Reset")

    try:
        settings = load_settings()

        if settings is None:
            raise FileNotFoundError("The settings file was not found. Run `uv run setup` first.")

        new_settings = prompt_for_settings(existing_settings=settings)

        new_settings.ignore_files.add(new_settings.output_path.name)

        save_settings(new_settings)

        success("Settings file reset completed")
    except (FileNotFoundError, SettingsLoadError, SettingsSaveError) as exc:
        error(f"Reset error: {exc}")

        raise SystemExit(1) from exc
    except (KeyboardInterrupt, EOFError):
        info("Settings file reset cancelled")

        raise SystemExit(130) from None
