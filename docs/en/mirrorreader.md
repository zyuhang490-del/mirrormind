# MirrorReader

[English index](README.md) | [Chinese source](../../MirrorReader/README.md) | [Development guide](mirrorreader-development-guide.md)

MirrorReader is a minimal reading prototype for MirrorMind. It starts with a specific problem: making it easier to return after an interruption. Development begins with a small working program.

## Current stage: stage 1

The implemented script provides basic paragraph navigation:

- Read a UTF-8 TXT file.
- Separate paragraphs at blank lines.
- Display the current paragraph and total count.
- Move to the previous or next paragraph using commands.
- Prevent navigation beyond the first and last paragraphs.
- Exit through a command.

The current version does not save progress, notes, or cognitive snapshots. Those are later milestones.

## Run

Requires Python 3.10 or newer. From the repository root:

~~~powershell
python MirrorReader/main.py
~~~

Or enter the MirrorReader directory and run:

~~~powershell
python main.py
~~~

The default article is sample_data/sample_article.txt relative to the script directory. You can supply your own UTF-8 TXT file:

~~~powershell
python MirrorReader/main.py "path/to/article.txt"
~~~

**English edition note:** the application messages, help text, and bundled article are currently Chinese. Supplying English text lets you read English content; the interface language does not change. This documentation edition does not modify the program.

## Commands

| Command | Action |
| --- | --- |
| n | Next paragraph |
| p | Previous paragraph |
| s | Show current progress |
| help | Show help |
| exit | End the current session |

## Scope

The planned V0 excludes login, cloud synchronization, web scraping, OCR, a graphical interface, automatic state recognition, and autonomous agents. See the [development guide](mirrorreader-development-guide.md) for the complete proposal and later stages.

Source snapshot read October 27, 2026.
