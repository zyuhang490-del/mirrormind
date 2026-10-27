# MirrorMind

[简体中文](README.md) | **English**

> A personal cognitive terminal for human–computer collaboration: helping tools adapt to a person's intentions, state, and real environment, while keeping that person in charge of their purposes.

MirrorMind explores how personal software could help people understand and develop their potential, reconnect with earlier ideas, and reduce the unnecessary effort between an intention and an actual creation. Its guiding direction is **explore inward, connect outward**.

This repository contains an evolving design and research archive, alongside **MirrorReader**, an early Python command-line prototype. The broader cognitive system is a long-term proposal. It has not been implemented or validated as a complete product.

## Start here

For a first review, read this page, the [MirrorReader overview](docs/en/mirrorreader.md), and the [architecture assessment](docs/en/architecture-assessment.md). For the conceptual foundation, continue with the [initial manifesto](docs/en/initial-manifesto.md) and the [self-structuring mechanism](docs/en/self-structuring.md).

| English document | What it covers |
| --- | --- |
| [Documentation index and translation coverage](docs/en/README.md) | Reading order, Chinese sources, and what is available in English |
| [Initial manifesto](docs/en/initial-manifesto.md) | Humanist foundations, core concepts, three-layer architecture, and design principles |
| [Self-structuring and reverse state identification](docs/en/self-structuring.md) | Revisable state hypotheses, descriptive remainder, temporary executable structures, and feedback |
| [Technical mapping](docs/en/technical-mapping.md) | Proposed engineering components and the evolution of the design |
| [Architecture assessment](docs/en/architecture-assessment.md) | Feasibility, reward signals, cold start, risks, and the revised MVP |
| [Foundational questions](docs/en/foundational-questions.md) | Unresolved philosophical and epistemological constraints |
| [Foundational question 2](docs/en/symbolic-representation.md) | Acting with incomplete representations without equating a model with a person |
| [MirrorReader overview](docs/en/mirrorreader.md) | What the prototype currently does and how to run it |
| [MirrorReader development guide](docs/en/mirrorreader-development-guide.md) | Planned V0, incremental milestones, testing, and evaluation |
| [Research and archive guide](docs/en/research-guide.md) | Literature, further reading, learning records, and original archives |
| [Terminology](docs/en/glossary.md) | Consistent English translations of the project's central concepts |

## Vision and current implementation

| Area | Current status |
| --- | --- |
| Project philosophy and architecture | Written proposals under revision |
| Reading a UTF-8 TXT file and navigating paragraphs | Implemented in MirrorReader |
| Saving and restoring reading progress | Planned; not implemented in the current prototype |
| Cognitive snapshots, notes, and reading modes | Planned |
| Cross-time retrieval and inspiration connections | Research and product hypotheses |
| Adaptive self-structuring and feedback learning | Design proposal; awaiting a minimal validation loop |
| General operating-system integration, wearables, and neural interfaces | Long-term exploratory directions |

## Run the prototype

Use Python **3.10 or newer**. No third-party packages are needed by the current script.

From the repository root:

~~~powershell
python MirrorReader/main.py
~~~

Or supply your own UTF-8 text file:

~~~powershell
python MirrorReader/main.py "path/to/article.txt"
~~~

The default sample text, terminal messages, and help output are currently in Chinese. Commands use ASCII text:

| Command | Action |
| --- | --- |
| n | Next paragraph |
| p | Previous paragraph |
| s | Show current position |
| help | Show help |
| exit | End the session |

The program separates paragraphs at blank lines. Current sessions do not persist progress.

## How the proposed system fits together

~~~text
User-authorized storage of events, expressions, failures, and unexplained material
    → provisional human–environment state representations
    → cross-time resonance / inspiration connections
    → reverse state identification when observations challenge expectations
    → temporary executable structures shaped by intention and available capabilities
    → execution, user correction, and learning across sessions
~~~

The user remains the **intention-end**: the person determines the ends, while the system learns how to support them. Observed data, inferred states, and the person themselves must remain distinct. Users must be able to inspect, correct, delete, or reset the system's representations.

Success should be assessed through renewed task engagement, understanding, and useful output. The design rejects engagement time, clicks, and dependency as its primary objectives.

## Reviewing or contributing

Useful contributions include challenging assumptions, defining falsifiable prototype experiments, improving the small reading prototype, and correcting translations. Please anchor proposals in a concrete scenario and explain what observation would support or contradict them.

The English edition preserves the historical character of the design. Earlier feasibility claims, schedules, and proposed technology stacks are dated author assessments, not fresh technical endorsements or delivery commitments. See each document's editorial notes.

The Chinese Markdown files remain the source for this edition. The English material reflects the local source snapshot prepared on **October 27, 2026**, including the conceptual revisions dated **October 7, 2026**. See the [coverage index](docs/en/README.md) for translations, adapted guides, and Chinese-only archives.

## Repository document format

As of October 28, 2026, published documentation uses Markdown. Word and PDF originals and intermediate OCR text are kept locally and excluded from future commits. Historical source content converted from Word remains available as Markdown snapshots. The runtime TXT sample and machine-readable RIS bibliography keep their original formats. See the [literature index](思想文献/README.md) for full-text, excerpt, discussion-only, and missing-transcription labels.
