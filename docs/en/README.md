# English documentation

[Repository overview](../../README.en.md) | [中文首页](../../README.md)

This edition gives English-speaking reviewers a route through MirrorMind's project design and its current prototype. Prepared October 27, 2026, from the local Chinese Markdown sources, including changes that had not yet been committed when translation began. The English text and the Chinese originals are maintained separately; there is no automatic synchronization.

## Reading order

1. [Repository overview](../../README.en.md): purpose and implementation status.
2. [MirrorReader](mirrorreader.md): the working prototype and its limits.
3. [Architecture assessment](architecture-assessment.md): risks and validation boundaries.
4. [Initial manifesto](initial-manifesto.md): original motivation and architecture.
5. [Self-structuring](self-structuring.md): the revised core mechanism.
6. [Technical mapping](technical-mapping.md): engineering interpretations and historical roadmap.
7. [Foundational questions](foundational-questions.md) and [question 2](symbolic-representation.md): unresolved constraints.
8. [Development guide](mirrorreader-development-guide.md): the incremental implementation plan.
9. [Research guide](research-guide.md) and [glossary](glossary.md): archive navigation and terminology.

## Source mapping and coverage

“Translation” means the substantive sections of the source are rendered in English, with editorial qualifications explicitly separated. “Adapted guide” means a navigation or review aid, not a full translation of every linked source.

| English file | Chinese source | Treatment |
| --- | --- | --- |
| [Repository overview](../../README.en.md) | [Root README](../../README.md), [prototype README](../../MirrorReader/README.md), and current prototype code | Adapted team-facing overview |
| [Initial manifesto](initial-manifesto.md) | [Initial design](../../Mirrormind设计文档/初始设计文档/初始设计文档.md) | Translation |
| [Self-structuring](self-structuring.md) | Core mechanism (local Chinese draft: `Mirrormind设计文档/自结构与状态逆识别.md`; not included in this commit) | Translation |
| [Technical mapping](technical-mapping.md) | [Engineering mapping](../../Mirrormind设计文档/技术映射/技术映射.md) | Translation with historical notes |
| [Architecture assessment](architecture-assessment.md) | [Assessment](../../Mirrormind设计文档/架构评估_合理性与可行性.md) | Translation with historical notes |
| [Foundational questions](foundational-questions.md) | [Question index](../../Mirrormind底层元问题集/README.md) | Translation |
| [Question 2](symbolic-representation.md) | Symbolic representation (local Chinese draft: `Mirrormind底层元问题集/元问题2：符号系统如何在不可完全表示人的前提下参与自结构.md`; not included in this commit) | Translation |
| [MirrorReader overview](mirrorreader.md) | [Prototype README](../../MirrorReader/README.md) | Translation, with a root-level run command and current UI note |
| [Development guide](mirrorreader-development-guide.md) | [Development guide](../../MirrorReader/MirrorReader开发指引.md) | Translation; planned features explicitly distinguished from current code |
| [Research and archive guide](research-guide.md) | [Research background](../../Mirrormind设计文档/视野拓展与专业积淀/视野拓展与专业积淀.md), [reading roadmap](../../Mirrormind设计文档/视野拓展与专业积淀/阅读路线图.md), literature and learning folders | Adapted guide; individual archive documents remain in Chinese |
| [Glossary](glossary.md) | Terminology used across the design documents | Editorial terminology aid |

The research-background essay, detailed reading roadmap, personal learning records, historical source snapshots, and third-party literature translations have **not** been translated in full in this edition. The research guide identifies those materials and their limitations. This is an English project-documentation edition, not a second repository or a claim that every archived file is bilingual.

## Editorial conventions

- Retain the author's philosophical positions and speculative concepts as proposals, rather than converting them into established findings.
- Preserve original dates. The translation date does not make a historical technical assessment current.
- Mark added qualifications as **Editorial note**. These help distinguish historical claims, design goals, and implemented features.
- Use [the glossary](glossary.md) consistently, especially for self-structuring, descriptive remainder, and inspiration connection.
- Link back to Chinese source documents and keep existing filenames and directories intact.
- When updating an English translation, compare the complete Chinese source again and update its source snapshot note. These translations currently track the October 7, 2026 concept revision, as read locally on October 27, 2026.

## Archive format update — October 28, 2026

Word originals have Markdown transcriptions or historical snapshots. PDF originals and intermediate OCR TXT files are local-only. Some literature topics still have only excerpts or discussion notes; their status is explicit in the [literature index](../../思想文献/README.md). The archival originals remain available locally and in earlier Git history.
