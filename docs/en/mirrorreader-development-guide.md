# MirrorReader Development Guide

[English index](README.md) | [Chinese source](../../MirrorReader/MirrorReader开发指引.md) | [Current implementation](mirrorreader.md)

English edition prepared October 27, 2026.

This is the development plan for a small MirrorMind prototype. A real, runnable project should test whether cognitive continuity and tools that change with state can reduce learning resistance.

**Implementation note:** V0 below is a target. The current program has reached paragraph navigation only. Progress persistence, notes, snapshots, and reading modes are planned, even when this guide describes their intended behavior in the present tense.

## 1. Project positioning

MirrorReader is conceived as a personal reading tool that saves progress, records context, and changes the reading approach according to the current state.

Its starting scenario is someone abandoning an Economist article, technical text, or course material because it is difficult, the goal is vague, lookup steps are scattered, or interruptions make resumption hard.

It leaves life goals to the user and initially addresses three testable questions:

1. Can the user quickly recover the previous cognitive context after interruption?
2. Can the same material support different learning structures for different present states?
3. Can questions, expressions, and ideas from reading become useful again later?

## 2. Design principles

### 2.1 Allow vague goals

A user can begin with “I want to study this article” without deciding whether to focus on vocabulary, sentence patterns, or ideas. Goals can form during reading.

### 2.2 Preserve the person's authority

The system can recommend a mode; the first version lets the user choose. Do not claim to have recognized emotion or cognition without evidence.

### 2.3 Save the process as well as results

Alongside position, preserve mode, questions, interests, interruption reason, and next entry point.

### 2.4 Reduce friction before adding intelligence

If the version without a language model does not make reading easier, adding AI can conceal a product problem.

### 2.5 Avoid dependency metrics

Do not make opens, dwell time, or streaks the highest objective. Measure resumption, understanding, and useful output.

## 3. Exclusions from V0

V0 excludes automatic emotion or cognitive-state recognition; camera, keyboard, or screen monitoring; PDF ingestion, scraping, or OCR; login, synchronization, or multiple users; vector databases and knowledge graphs; complex automatic notes; Electron or a full GUI; control of other applications; and autonomous agents.

These directions may be explored later. They should not block the first testable version.

## 4. Intended V0 experience

~~~text
Launch
    → select a local TXT article
    → restore the previous position and context
    → choose relaxed / normal / deep reading
    → read paragraph by paragraph; record words, questions, or ideas
    → give a one-sentence reason for stopping
    → generate a next entry point and save a cognitive snapshot
~~~

On reopening, a snapshot might say:

~~~text
Last time you reached paragraph 12 in normal mode.
You focused on the author's expressions of causality.
You stopped because you had a class.
Continue with paragraph 13, or first review the saved expression.
~~~

## 5. Three reading modes

Complex algorithms are unnecessary for V0. Different interfaces and prompts can test an initial form of self-structuring.

### Relaxed reading

Show longer passages, avoid unsolicited vocabulary lookup, and keep “save this” and “continue” prominent. Support continuity and contact with the material.

### Normal study

Show one paragraph, offer vocabulary, expression, and question notes, and occasionally ask whether a recap would help. Support comprehension and a small amount of reusable language.

### Deep analysis

Show one paragraph, prompt attention to claims, evidence, structure, and expression, and allow longer analysis. Support an understanding that can become an output.

The user chooses. Later suggestions can consider available time, earlier choices, and feedback, with an easy override.

## 6. Planned V0 checklist

The following checklist translates the target specification; it is not an implementation status report.

- [ ] Read UTF-8 TXT files and split at blank lines.
- [ ] Show current paragraph and total count.
- [ ] Support previous and next paragraph.
- [ ] Save position at exit and restore it at launch.
- [ ] Select a reading mode at the start.
- [ ] Record vocabulary, questions, and ideas.
- [ ] Record why reading stopped.
- [ ] Write a cognitive snapshot.
- [ ] Keep data in local JSON.

Afterward, consider history search, session summaries, dictionary or model APIs, resurfacing earlier fragments, and a GUI.

## 7. Suggested directory structure

This is a proposed structure, not a listing of the current repository:

~~~text
MirrorReader/
├── README.md
├── main.py
├── sample_data/
│   └── sample_article.txt
├── private_data/
│   ├── articles/
│   └── reader_state.json
├── tests/
│   └── test_reader.py
└── .gitignore
~~~

Begin with main.py. Split only when it grows to roughly 150–200 lines or responsibilities become confusing:

~~~text
main.py       entry point and command loop
reader.py     paragraph splitting and navigation
storage.py    JSON loading and saving
session.py    sessions and cognitive snapshots
tests/        relevant tests
~~~

Do not split into many files just to appear professional.

## 8. Data design

One JSON file is sufficient for V0:

~~~json
{
  "current_article": "economist_example.txt",
  "articles": {
    "economist_example.txt": {
      "position": 12,
      "total_paragraphs": 36,
      "last_mode": "normal",
      "next_entry": "Continue at paragraph 13 and focus on causal expressions",
      "notes": [
        {
          "type": "expression",
          "paragraph": 10,
          "content": "give rise to",
          "created_at": "2026-08-02T20:30:00"
        }
      ],
      "sessions": [
        {
          "started_at": "2026-08-02T20:00:00",
          "ended_at": "2026-08-02T20:35:00",
          "mode": "normal",
          "start_position": 7,
          "end_position": 12,
          "focus": "Sentence patterns expressing causality",
          "stop_reason": "Needed to go to class",
          "next_entry": "Continue from paragraph 13"
        }
      ]
    }
  }
}
~~~

This is an illustrative first schema. Avoid designing a database for every hypothetical future need.

**Editorial note:** the source does not define whether stored positions are zero- or one-based. Decide and document that convention before implementation; do not treat this example as a finalized storage contract.

## 9. Proposed command-line interaction

These include future commands beyond stage 1:

| Command | Intended action |
| --- | --- |
| n | Next paragraph |
| p | Previous paragraph |
| w word | Record a word or expression |
| q text | Record a question |
| i text | Record an idea |
| s | Show progress |
| notes | Show notes for this article |
| exit | Save and exit |
| help | Show help |

Start parsing with straightforward string comparisons:

~~~python
command = input("> ").strip()

if command == "n":
    ...
elif command.startswith("w "):
    ...
~~~

This naturally exercises loops, conditionals, strings, and functions.

## 10. Incremental development

Advance after acceptance checks, rather than rushing against dates.

| Stage | Work | Learning | Acceptance criterion |
| --- | --- | --- | --- |
| 0: define the problem | Write a README explaining reading difficulties, intended friction reduction, V0 scope, and launch instructions | Requirements and Markdown | A non-programmer understands the problem |
| 1: continuous navigation | Read TXT, split paragraphs, accept commands in a loop, track position, support previous/next/exit | Files, strings, lists, loops, conditions, indexing | Read the sample from start to finish without crossing boundaries |
| 2: resume after exit | Learn dictionaries, save JSON, detect and restore state, handle damaged files clearly | Dictionaries, JSON, paths, exceptions, functions | Reopen a terminal and continue at the correct paragraph |
| 3: cognitive snapshots | Select a mode; save words, questions, ideas, stop reason, positions, focus, next entry; show the last snapshot | Function boundaries, lists of dictionaries, time, validation | Reopen the next day without reconstructing why reading stopped |
| 4: modes really differ | Reduce operations in relaxed mode, expose common notes in normal mode, prompt argument analysis in deep mode, log mode switches | Program state, configuration dictionaries, avoiding duplication | The same article offers meaningfully different interactions |
| 5: real validation | Use it for 7–14 sessions, without requiring daily streaks | Observation and product evaluation | Identify effective and ineffective features from records |

For each validation session record time to start reading, paragraphs read, context recovery, remaining difficulties, extra burden, and reusable expressions or ideas.

## 11. Testing checklist

Manual checks are acceptable initially.

**Files:** empty text, one paragraph, mixed Chinese and English, missing file, incorrect encoding.

**Navigation:** previous on the first paragraph, next on the last, unknown command, empty input.

**State, after stage 2:** no JSON on first run, reopen after a normal save, missing fields, damaged JSON, and switching articles then returning.

After stage 2, learn pytest and prioritize paragraph splitting and progress-restoration logic that can be tested without an interactive session.

## 12. Git practice

Commit when a working feature is complete:

~~~text
docs: describe MirrorReader v0 scope
feat: load and split text article
feat: navigate between paragraphs
feat: save reading position to json
feat: restore previous reading session
feat: record words questions and ideas
fix: prevent position from exceeding article range
~~~

Before each commit, run it yourself, inspect git diff, and check for API keys, private articles, and personal records.

Suggested ignore entries:

~~~gitignore
__pycache__/
.venv/
private_data/
.env
~~~

The source warns that Economist articles may be copyrighted. Public sample texts should be self-written or clearly permitted for redistribution.

## 13. Using AI while learning

Use AI as a teacher and pair partner. Keep requests small, for example:

~~~text
I have just learned Python loops and need to split a text at blank lines.
First explain the concepts, then give an example under 15 lines.
Give me an exercise to implement myself instead of completing the project for me.
~~~

For debugging, provide the goal, current code, full error, and attempted fixes.

Before accepting generated code, be able to explain each function, the path data takes into and out of the program, the variables controlling behavior, and where an error is likely to occur. If you cannot, reduce the task size.

## 14. V1: restrained model integration

Only after V0 proves useful, add an OpenAI-compatible API for:

1. Explaining an expression the user actively selects in the current paragraph.
2. Offering explanations at a depth appropriate to the selected mode.
3. Compressing already-recorded session notes into a next entry point.

Avoid default whole-article summaries: they may bypass the reading and fail to test understanding.

A proposed output shape is:

~~~json
{
  "meaning_in_context": "",
  "common_usage": "",
  "example": "",
  "one_question": ""
}
~~~

Keep keys in environment variables or a local .env file, never in code or Git.

## 15. V2: a small inspiration-connection experiment

After accumulating snapshots, first connect records with simple rules: shared keywords, note types, themes, unresolved questions, or expressions marked for future use.

For example:

~~~text
You are considering how technology affects human agency.
Seventeen days ago, you recorded an opposing view while reading another article.
Would you like to view them side by side?
~~~

Consider embeddings and vector retrieval after users demonstrate that such connections are useful.

## 16. V3: returning from MirrorReader to MirrorMind

| Reading prototype | General concept |
| --- | --- |
| Reading material | Current task object |
| Reading mode | Explicit cognitive state |
| Reading progress | Task continuity |
| Session snapshot | Cognitive snapshot in comprehensive storage |
| Reappearance of historical fragments | Inspiration connection |
| Mode-dependent interface changes | Initial self-structuring |
| Vocabulary and note tools | Atomic capability invocation |

Then replace reading with programming, writing, or research and test whether the structure transfers.

## 17. Evaluation

Avoid claiming improved creativity from one score. Observe:

- **Recovery cost:** time from opening to actual reading.
- **Continuity:** whether resumption accurately reconnects with the interrupted task.
- **Completion:** paragraphs actually read per session.
- **Useful accumulation:** expressions and ideas later reused.
- **Tool friction:** external tool switches per session.
- **Subjective burden:** a 1–5 report of additional burden.
- **Conversion into output:** whether reading informs imitation exercises, articles, code, or decisions.

Success means that when someone chooses to return, the system helps them resume.

## 18. Main risks

| Risk | Response |
| --- | --- |
| Rebuilding a complex note application | Require evidence that a feature shortens recovery and continuation |
| AI does too much and learning suffers | Explain user-selected portions by default and encourage the user's own interpretation first |
| Recording becomes a burden | Let users leave notes blank; initially request only a one-sentence stop reason |
| State estimation is presented as mind reading | Use explicit choices in V0; later show evidence and uncertainty |
| The project expands too early | Complete real V0 validation before web/mobile clients, vector databases, or autonomous agents |

## 19. Learning map

| Project task | Python / engineering knowledge |
| --- | --- |
| Command loop | while, if/elif, input/output |
| Paragraph splitting | Strings, lists, indexing |
| Navigation | Functions and boundary conditions |
| Saving progress | Dictionaries, JSON, file I/O |
| Recording notes | Lists of dictionaries and time |
| Error handling | try/except |
| Splitting files | Modules, imports, responsibilities |
| Automated tests | pytest and pure functions |
| API calls | HTTP, JSON, environment variables |
| Multiple articles | Identifiers, paths, data modeling |
| Vector retrieval | Embeddings, similarity, databases |

Let the current project problem guide targeted learning alongside the broader curriculum.

## 20. Definition of V0 completion

V0 is complete only when:

- A new user can run it from the README.
- Reading, navigation, saving, and restoration work.
- Three note categories are supported.
- The previous cognitive snapshot is saved and displayed.
- The three modes differ at least in interaction structure.
- Empty files, navigation limits, and damaged state receive basic handling.
- Keys and private material are absent from the code.
- At least seven real reading sessions have been completed.
- A validation report identifies what worked, what did not, and the next step.

## 21. The original first step

The source proposes creating a MirrorReader directory on drive D, initializing Git, adding README.md, main.py, and a public sample text, then reading the file and printing a paragraph count before the first commit.

~~~text
Run main.py
    → read sample_article.txt successfully
    → print “Found N paragraphs”
~~~

**Editorial note:** the folder and initial navigation program already exist in this repository. This passage preserves the original learning sequence; do not initialize a nested repository merely to follow it literally.

Stop at a small milestone, understand every line, then continue. The first step toward MirrorMind is a program its developer can explain, modify, and keep improving.
