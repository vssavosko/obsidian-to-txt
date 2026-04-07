"""Interactive CLI prompts for creating or updating export settings."""

from pathlib import Path

from rich.prompt import Prompt

from obsidian_to_txt.models import Settings


def prompt_for_settings(existing_settings: Settings | None = None) -> Settings:
    """Prompt user for export settings and return a normalized Settings instance."""
    vault_path_default = (
        str(existing_settings.vault_path) if existing_settings else "/Users/username/vault"
    )
    output_path_default = str(existing_settings.output_path) if existing_settings else "vault.txt"
    ignore_directories_default = (
        ",".join(existing_settings.ignore_directories)
        if existing_settings
        else ".git,.obsidian,templates"
    )
    ignore_files_default = (
        ",".join(existing_settings.ignore_files)
        if existing_settings
        else f".env,.gitignore,{Path(output_path_default).name}"
    )

    vault_path_raw = Prompt.ask("Vault path", default=vault_path_default)
    output_path_raw = Prompt.ask("Output path", default=output_path_default)
    ignore_directories_raw = Prompt.ask(
        "Ignore directories (comma-separated)",
        default=ignore_directories_default,
    )
    ignore_files_raw = Prompt.ask(
        "Ignore files (comma-separated)",
        default=ignore_files_default,
    )

    ignore_directories = {
        directory.strip() for directory in ignore_directories_raw.split(",") if directory.strip()
    }
    ignore_files = {file.strip() for file in ignore_files_raw.split(",") if file.strip()}

    return Settings(
        vault_path=Path(vault_path_raw),
        output_path=Path(output_path_raw),
        ignore_directories=ignore_directories,
        ignore_files=ignore_files,
    )
