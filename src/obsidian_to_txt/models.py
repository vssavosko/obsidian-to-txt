"""Domain models shared across setup, persistence, and export flows."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Settings:
    """User-defined settings for Obsidian vault export.

    Attributes:
        vault_path: Path to the root directory of the Obsidian vault.
        output_path: Target text file path for the merged export.
        ignore_directories: Directory names to skip during recursive traversal (e.g., `.git`, `.obsidian`, `templates`).
        ignore_files: File names to skip (e.g., `.env`, `.gitignore`, the export output file itself).
    """

    vault_path: Path
    output_path: Path
    ignore_directories: set[str]
    ignore_files: set[str]


@dataclass(slots=True)
class ExportStatistics:
    """Counters that describe the export run outcome.

    Attributes:
        exported_files: Number of Markdown files successfully written to output.
        skipped_files: Number of files skipped (non-Markdown or ignored by name).
        failed_files: Number of Markdown files that could not be read.
    """

    exported_files: int = 0
    skipped_files: int = 0
    failed_files: int = 0
