"""Export Markdown notes from an Obsidian vault into a single plain-text file."""

import os
from pathlib import Path

from obsidian_to_txt.models import ExportStatistics


def export_vault_to_text(
    vault_path: Path,
    output_path: Path,
    ignore_directories: set[str],
    ignore_files: set[str],
) -> ExportStatistics:
    """Export vault notes into a single plain-text file."""
    statistics = ExportStatistics()

    with output_path.open("w", encoding="utf-8") as outfile:
        for root, directories, files in os.walk(vault_path):
            directories[:] = sorted(
                directory for directory in directories if directory not in ignore_directories
            )

            for file in sorted(files):
                if not file.endswith(".md") or file in ignore_files:
                    statistics.skipped_files += 1

                    continue

                file_path = Path(root) / file
                relative_file_path = file_path.relative_to(vault_path)

                try:
                    content = file_path.read_text(encoding="utf-8")
                except (OSError, UnicodeDecodeError):
                    statistics.failed_files += 1

                    continue

                outfile.write(f"\n\n--- START OF THE FILE: {relative_file_path} ---\n\n")
                outfile.write(content.rstrip())
                outfile.write(f"\n\n--- END OF THE FILE: {relative_file_path} ---\n\n")

                statistics.exported_files += 1

    return statistics
