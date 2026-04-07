"""Rich utilities."""

from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def title(text: str) -> None:
    """Print a title."""
    console.print(Panel.fit(text, border_style="cyan", padding=(0, 1)))


def info(text: str) -> None:
    """Print an info message."""
    console.print(f"[cyan]💬[/] {text}")


def success(text: str) -> None:
    """Print a success message."""
    console.print(f"[bold green]✅[/] {text}")


def warn(text: str) -> None:
    """Print a warning message."""
    console.print(f"[yellow]⚠️[/] {text}")


def error(text: str) -> None:
    """Print an error message."""
    console.print(f"[bold red]❌[/] {text}")


def settings_preview(
    vault_path: Path,
    output_path: Path,
    ignore_directories: set[str],
    ignore_files: set[str],
) -> None:
    """Print the settings preview."""
    table = Table(title="Settings")

    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("Vault path", str(vault_path))
    table.add_row("Output path", str(output_path))
    table.add_row("Ignore directories", ", ".join(sorted(ignore_directories)) or "-")
    table.add_row("Ignore files", ", ".join(sorted(ignore_files)) or "-")

    console.print(table)


def export_summary(
    exported: int,
    skipped: int,
    failed: int,
    output_path: Path,
) -> None:
    """Print the export summary."""
    table = Table(title="Export Summary")

    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right")

    table.add_row("Exported", str(exported))
    table.add_row("Skipped", str(skipped))
    table.add_row("Failed", str(failed))
    table.add_row("Output path", str(output_path))

    console.print(table)
