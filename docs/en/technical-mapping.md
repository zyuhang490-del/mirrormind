# Technical Mapping and Evolution Roadmap

[English index](README.md) | [Chinese source](../../Mirrormind设计文档/技术映射/技术映射.md)

Original archive: 技术映射.docx, retained in the Chinese source directory. Markdown conversion: July 27, 2026. Concept update: October 7, 2026. English edition: October 27, 2026.

**Editorial note:** Maturity ratings, named stacks, schedules, and feasibility statements below are historical author assessments. They have not been independently revalidated for this translation. The October 7 revision and the small [MirrorReader prototype](mirrorreader.md) define the current direction more accurately than the early whole-desktop proposal.

## 0. Principle: no magic

The source follows a “no magic” principle: proposed capabilities should map to available technologies or identifiable research directions. Its purpose is engineering assembly and evolution, without assuming future breakthroughs.

**October 7 revision:** self-structuring has expanded from dynamic templates and tool calls into a loop containing human–environment state representation, descriptive remainder, reverse state identification, structure compilation, and feedback learning. Early mappings are retained as a record of development. Current definitions are in [Self-structuring](self-structuring.md).

## 1. Mapping the long-term concepts

| Philosophical concept | Proposed technical mapping in the source | Historical maturity assessment |
| --- | --- | --- |
| Dynamic probability cloud | Continual and online learning: update a model over a data stream | A research frontier with early industrial exploration |
| Cracks and background noise | Anomaly detection in personal activity streams | Established methods whose transfer to personal cognition needs work |
| Inverse structure model | A personal baseline model, adapted from a general base, whose prediction errors reveal cracks | Presented as a promising path and an active research topic |
| Two-layer storage and self-structuring | Unstructured data lake, vector database, and knowledge graph | Storage components described as mature and engineerable |
| Transcendental reasoning | Retrieval-augmented generation and prompting over personal history | Components described as mature |
| Activation function | Recommender logic applied to earlier fragments of a person's own history | Algorithmic foundations described as mature; intended application remains exploratory |

**Editorial note:** A mapping identifies candidate components. It does not demonstrate that they realize the corresponding philosophical concept, or that mature storage establishes mature self-structuring.

## 2. Mapping the three architecture layers

### Stability layer → activity recognition

The source proposes beginning with non-invasive sensing—screenshots, application-switching logs, keyboard and mouse interaction streams, or camera-based gaze tracking—in place of the long-term brain–computer interface. A lightweight classifier would estimate broad states such as writing, reading, or being stuck.

The source rates data collection and classification techniques as mature. Their ability to infer a particular user's intention reliably remains a separate validation question.

### Adaptive layer → a personal data lake and retrieval-augmented generation

The early proposal implements comprehensive storage as a local unstructured data lake. A background process would continuously record desktop streams such as window titles, OCR text, and audio transcripts into cognitive-snapshot logs.

Structured storage and inspiration connections would use a local vector database. An offline process embeds snapshots; when requested, the current snapshot becomes a retrieval query and related records are presented as possible inspiration.

The source rates logging, embeddings, vector storage, and similarity search as mature components.

**Editorial note:** Continuous monitoring is the early proposal, not the current prototype's behavior. The revised design limits storage by informed authorization, purpose, deletion, and forgettability. Similarity results do not by themselves demonstrate inspiration.

### Self-structuring control layer → representation, compilation, and feedback

The revised layer can be divided into five independently testable components:

| Component | Minimum technical form | Current design objective |
| --- | --- | --- |
| Events and comprehensive storage | JSON or SQLite event logs with source, time, and permissions | Record inputs, structures, outcomes, and corrections without continuous surveillance |
| State representation | Explicit fields separating observation, interpretation, alternatives, and remainder | Make representations machine-operable, understandable, and editable |
| Environmental capability registry | A registry of files, programs, CLI commands, APIs, and tools | Register a few explicit tools before considering whole-computer control |
| Structure compiler | Rules plus model-generated candidate workflows or interface configurations | Generate reversible temporary structures from intention, state, and environment |
| Feedback learning | Explicit feedback, corrections, task continuation, and strategy scores | Update memory and rules before considering a personal large model |

The first question is whether the same material can produce different, explainable, editable structures under different intentions and states. When observations challenge predictions, the system should retain remainder and try a simplified reverse-state-identification process.

- **Local feasibility:** event logging, state objects, candidate structures, explicit feedback, and bounded tool use can be implemented.
- **System-wide feasibility:** general environment recognition, reliable long-term online learning, interfaces spanning multiple applications, and safe permission governance require further iteration and validation.

## 3. Engineering breakdown of the early document prototype

The source proposes the following stack for a self-structuring document editor:

| Component | Proposed choice | Role |
| --- | --- | --- |
| Application framework | Electron + React | Desktop shell and frontend |
| Local data lake | CSV / JSON logs | Cognitive-snapshot metadata |
| Cloud model | OpenAI API / Anthropic API | Language-model capabilities |
| Local model | Ollama + an open embedding model | Offline processing for sensitive material |
| Vector database | Chroma, via Python | Lightweight embedded retrieval |
| Model orchestration | LangChain | Connect models, retrieval, and dynamic-template generation |
| Intention sensing | Python background scripts | Read system events, active applications, and window titles |

The historical source estimates **4–8 weeks** for an engineer with full-stack experience to assemble the components.

**Editorial note:** This is an unvalidated early estimate, not a delivery commitment, benchmark, or estimate for the current student developer. The running MirrorReader script uses Python's standard library and does not depend on this stack.

## 4. Historical roadmap: “2024–2030”

The source gives that calendar label while also listing durations extending beyond it. The inconsistency is preserved here as part of the historical record; the table is an exploratory sequence rather than a current schedule.

| Stage | Source duration | Name | Core task | Intended validation |
| --- | --- | --- | --- | --- |
| I | 1–2 years | Intention-aware assistant | Activity recognition from desktop streams; initial stability layer | Feasibility of nonverbal intention sensing |
| II | 2–4 years | Memory-indexed companion | Two-layer storage and inspiration connections | Whether connections reduce cognitive resistance |
| III | 4–7 years | Wearable mirror | Move sensing toward glasses or watches | Explore the core interaction paradigm |
| IV | More than 7 years | Neural-interface prototype | Minimally invasive interfaces and direct neural decoding | Explore the long-term conception |

The original final row anticipates inheriting earlier data and models fully. That is an aspiration requiring validation, not demonstrated portability.

## 5. The original proposed first step

The early source addresses its future engineer with three instructions:

1. Create a GitHub repository called MirrorMind.
2. Write a Python script, proposing psutil, to obtain the active window title every five seconds.
3. Save records as a timestamp and active window title.

The text presents the first log entry as the first small step toward the broader storage vision.

**Editorial note:** These are historical instructions, not a tested setup recipe. The source's active-window collection method and platform support were not verified here. The repository already exists, and the current implementation starts from explicit reading interactions instead. Follow the [MirrorReader guide](mirrorreader-development-guide.md) for that development path.
