"""CLI command for exporting an Obsidian vault into a single plain-text file."""

from rich.console import Console

from obsidian_to_txt.settings_store import (
    SettingsLoadError,
    load_settings,
)
from obsidian_to_txt.ui.rich import (
    error,
    export_summary,
    info,
    success,
    title,
)
from obsidian_to_txt.vault_to_text_exporter import export_vault_to_text


def main() -> None:
    """Run export using saved settings and print a Rich-formatted summary."""
    title("Obsidian to Text: Export")

    try:
        console = Console()
        settings = load_settings()

        if settings is None:
            raise FileNotFoundError("The settings file was not found. Run `uv run setup` first.")

        if not settings.vault_path.exists():
            raise FileNotFoundError(f"Vault path {settings.vault_path} does not exist")

        if not settings.vault_path.is_dir():
            raise NotADirectoryError(f"Vault path {settings.vault_path} is not a directory")

        info(f"Vault: {settings.vault_path}")
        info(f"Output: {settings.output_path}")

        with console.status("[bold green]Exporting vault...[/]"):
            statistics = export_vault_to_text(
                settings.vault_path,
                settings.output_path,
                settings.ignore_directories,
                settings.ignore_files,
            )

        success("Export completed")

        export_summary(
            statistics.exported_files,
            statistics.skipped_files,
            statistics.failed_files,
            settings.output_path,
        )
    except (FileNotFoundError, NotADirectoryError, SettingsLoadError) as exc:
        error(f"Export error: {exc}")

        raise SystemExit(1) from exc
    except (KeyboardInterrupt, EOFError):
        info("Export cancelled")

        raise SystemExit(130) from None
