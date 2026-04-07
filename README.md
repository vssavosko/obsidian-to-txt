# Obsidian to TXT

A tool for exporting notes from an Obsidian Vault into a single plain-text file.

The project helps you quickly combine Markdown note content into one `*.txt` file for:

- sharing with AI assistants and LLMs;
- knowledge base archiving;
- full-text search outside Obsidian;
- exporting notes to external systems.

## Features

- Interactive first-time setup via CLI.
- Local JSON-based configuration storage.
- Export all `*.md` files from a vault into a single output file.
- Ignore specific directories and files during export.
- Execution statistics: exported / skipped / failed.
- Friendly terminal UI powered by `rich`.

## Tech Stack

- **Language:** Python 3.13+
- **Environment and runner:** `uv`
- **CLI UI:** `rich`
- **Linting/formatting:** `ruff`
- **Type checking:** `ty`

## Requirements

- Python `>= 3.13`
- [uv](https://docs.astral.sh/uv/)

## Project Structure

```txt
src/obsidian_to_txt/
├── __init__.py
├── models.py                  # Data models
├── settings_store.py          # Settings persistence
├── vault_to_text_exporter.py  # Export logic
├── cli/
│   ├── setup.py               # First-time interactive setup command
│   ├── export.py              # Export command using saved settings
│   └── reset.py               # Reset settings command
└── ui/
    ├── prompts.py             # Interactive prompts for settings input
    └── rich.py                # Rich-based terminal output utilities
```

## Quick Start

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Run the initial setup:

   ```bash
   uv run setup
   ```

   During setup, the tool asks for:

   - `Vault path` - path to your Obsidian vault;
   - `Output path` - path to the resulting txt file;
   - `Ignore directories` - comma-separated directory names;
   - `Ignore files` - comma-separated file names.

   Settings are saved to:

   ```txt
   .config/obsidian-to-txt/settings.json
   ```

3. Start export:

   ```bash
   uv run export
   ```

> During setup and reset, the output file name is automatically added to ignored files to prevent self-inclusion.

## Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run ty check
```

## CLI Commands

### `uv run setup`

Runs first-time interactive setup and saves `settings.json` only if it does not already exist.

### `uv run export`

Runs export with saved settings and prints the export summary.

### `uv run reset`

Reruns interactive prompts using existing values as defaults and overwrites current settings.

## Output File Format

Each note is written to the output file with explicit start/end markers:

```txt
--- START OF THE FILE: path/to/note.md ---

...note content...

--- END OF THE FILE: path/to/note.md ---
```

## `settings.json` Example

```json
{
  "vault_path": "/Users/username/ObsidianVault",
  "output_path": "vault.txt",
  "ignore_directories": [".git", ".obsidian", "templates"],
  "ignore_files": [".env",".gitignore","vault.txt"]
}
```

## License

Licensed under MIT. See the [LICENSE](LICENSE) file for details.
