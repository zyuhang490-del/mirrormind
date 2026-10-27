# Self-Structuring and Reverse State Identification

[English index](README.md) | Chinese source (local Chinese draft: `Mirrormind设计文档/自结构与状态逆识别.md`; not included in this commit)

Status: core design supplement. Created October 7, 2026. English edition: October 27, 2026.

This document revises the meanings of cracks and background noise, the inverse structure model, two-layer storage, and self-structuring in the [initial manifesto](initial-manifesto.md). It develops the earlier conception toward mechanisms that can be explained, learned, and tested. The underlying epistemological question is discussed in [Foundational question 2](symbolic-representation.md).

## 1. Central claim

Self-structuring is more than invoking tools from an intention or generating a single workflow. It is a continuing process of human–environment co-adaptation:

> Within user-defined values, permissions, and revisable boundaries, the system forms an understanding of the person and operating environment, records states and feedback over time, learns ways to generate structures for that person, and compiles current intention, state, history, and environmental capabilities into temporary executable structures that can be revised and dissolved.

A “program structure” has software-like properties: it accepts inputs, performs processing, changes state, and produces outputs. Its specific modules, tools, interface, and execution paths are not fixed in advance.

The goal is to reduce the need for people to adapt to rigid applications, making intentions easier to realize in a real environment. The person remains the **intention-end**. The system learns and optimizes means while the person retains authority over final purposes.

## 2. Coupling in two directions

~~~text
From the environment upward:
hardware, OS, files, programs, compilers, CLI, APIs, permissions
                              ↘
                     temporary executable structure
                              ↗
From the person downward:
values, current intention, state, history, feedback, correction, confirmation
~~~

- **The environment supplies possibilities:** discover resources, limitations, and callable capabilities that actually exist now.
- **Human intention supplies direction:** the ability to do something does not by itself authorize action.
- **Protocols supply composition rules:** tool descriptions, formats, permissions, rollback, and confirmation make a temporary structure executable.
- **Feedback supplies learning signals:** outcomes and user corrections change future generation.

The model's role is closer to compiler, planner, and scheduler than to a central subject entitled to determine purposes.

## 3. Human–environment state representation

This layer sits between the person, environment, and executable program. It works with limited, revisable representations of traces a person leaves in context.

~~~text
Actual human state ≠ recorded data ≠ system interpretation ≠ compiled structure
~~~

State representations should be:

1. **Recordable:** preserve language, behavior, operations, environmental changes, and feedback as events.
2. **Storable:** retain necessary context across sessions and time.
3. **Readable:** revisit earlier states and outcomes when authorized.
4. **Processable:** support retrieval, comparison, aggregation, association, and pattern discovery.
5. **Compilable:** translate into constraints on interfaces, tools, data flows, and workflows.
6. **Machine-operable:** include structured fields, provenance, time, scope, and confidence.
7. **Communicable between human and machine:** render machine representations into understandable explanations.
8. **Interactive:** let users confirm, deny, or supplement judgments.
9. **Editable:** let users modify, delete, expire, or exclude a state category from future generation.
10. **Forgettable:** support revoked permissions, reduced weighting, and removal of derived models.

A state object should at least distinguish observation, interpretation, and proposed action:

~~~json
{
  "observation": {
    "event": "The user switched between several learning resources in a short period",
    "source": "local_activity",
    "timestamp": "2026-10-07T10:30:00+08:00"
  },
  "interpretation": {
    "hypothesis": "There may be a missing connection between knowledge and project actions",
    "confidence": 0.46,
    "alternatives": ["Actively comparing resources", "Collecting resources to postpone starting"],
    "scope": "The current learning task",
    "user_confirmed": false
  },
  "proposed_structure": {
    "action": "Offer a project map and one small coding entry point",
    "reversible": true,
    "requires_confirmation": false
  }
}
~~~

A single inference must not harden into a personality label. Machine operability must not be described as complete understanding of a person.

## 4. Two learning loops

### 4.1 Within-task loop

~~~text
Current intention + state representation + relevant history
+ environmental capabilities + permission boundaries
    → generate a temporary structure
    → execute, observe, and revise
~~~

This loop addresses how to carry out the present task.

### 4.2 Learning across time

~~~text
Which structure was adopted?
    → How did the user use, reject, or modify it?
    → Did the task actually advance?
    → Update interpretations and the generation strategy
    → Affect the next instance of self-structuring
~~~

The learning target is not a fixed set of user habits. It is how to organize information, tools, interfaces, and actions under particular intentions and conditions so that the person can advance their intention while retaining understanding, choice, and control.

Initially this learning can happen in event logs, state hypotheses, strategy scores, and memory. It does not imply continual modification of a large model's weights.

## 5. Descriptive remainder and failure descriptiveness

Every conversion from actual experience to symbols and then to executable structures leaves something out:

~~~text
Actual state → recorded data + observational remainder
Recorded data → state representation + encoding remainder
State representation → interpretation + interpretive remainder
Interpretation → program structure + compilation remainder
Program structure → execution result + realization remainder
~~~

A transformation should therefore return more than a single definite result:

~~~text
T(x) → (current result, descriptive remainder, uncertainty, scope)
~~~

- **Descriptive remainder:** what the current symbolic scheme has not explained or accommodated.
- **Failure descriptiveness:** the ability to explain where judgments fail, which assumptions they rely on, and what information is missing.
- **Generation uncertainty:** each temporary structure carries confidence, alternatives, reversibility, and points requiring confirmation.

Regression residuals offer a limited analogy: mismatches between prediction and observation can guide revision. Descriptive remainder must not all be treated as noise awaiting elimination. It can also reflect change, emerging intentions, contradiction, unformed ideas, or experience the present symbolic scheme cannot express adequately.

MirrorMind must retain a structural acknowledgment of what it does not know, instead of pursuing a final claim to understand the user completely.

## 6. Reverse state identification

The early inverse structure model searched for cracks through a personal baseline model's prediction errors. The revised mechanism examines the categories, relations, and representation scheme when observations contradict the current model.

~~~text
The current state model generates an expectation
    → observation contradicts expectation
    → retain descriptive remainder or an anomaly
    → suspend the existing label
    → propose alternative explanations
    → generate low-risk, reversible exploratory structures
    → distinguish explanations through user feedback and later outcomes
    → revise the state, its relations, or the state space itself
~~~

This process may reveal:

1. A previously unrecognized state.
2. An overlooked relationship between existing states.
3. A transition the user is undergoing.
4. An environmental constraint mistaken for a personal-state problem.
5. Failure of the symbolic scheme or classification method itself.

An anomaly begins an inquiry. It is neither automatically disposable noise nor a direct revelation of the true self.

## 7. Stable meta-structure and dynamic instances

A variable structure still requires a stable core.

**What must remain stable:**

- Identity, ownership, and permission boundaries.
- Tool-call protocols and data formats.
- Sources, time, confidence, and scope.
- Operation logs, rollback, and undo.
- Confirmation for irreversible actions.
- The user's ability to inspect, edit, delete, and reset models.
- Descriptions of failure and uncertainty.

**What can be generated dynamically:**

- Tools required for this task.
- Connections between tools and data.
- Workflow and interface organization.
- History to retrieve.
- Depth and order of presentation.
- Whether to execute, probe, offer alternatives, or ask.
- Structures to retain or dissolve after completion.

> MirrorMind has stable generation protocols and boundaries protecting human agency, while its executable instances can change with the coupled state of person and environment.

## 8. Relationships between core concepts

~~~text
Comprehensive storage
  retain events, raw expression, failed structures, unexplained remainder
    → State representation
      form provisional, machine-operable hypotheses users can understand and edit
    → Cross-time resonance / inspiration connection
      find history relevant to intention, state, and remainder
    → Reverse state identification
      use anomalies to reconsider states, relations, and representation
    → Self-structuring
      compile intention, state, history, capabilities, and remainder
    → Execution and feedback
      update state representations and generation strategies
~~~

Previously unexplained material can acquire meaning in a future context. It should not be forced prematurely into existing categories. This is one proposed source of cross-time resonance.

## 9. A compilation model

~~~text
Sₜ = Gθ(Iₜ, Hₜ, Eₜ, Cₜ, Mₜ, B, Rₜ)
~~~

| Symbol | Meaning |
| --- | --- |
| Iₜ | Current intention |
| Hₜ | Hypotheses about human state |
| Eₜ | Current hardware, software, files, and project environment |
| Cₜ | Callable capabilities and their connections |
| Mₜ | Relevant history and learned structural experience |
| B | Values, permissions, and confirmation rules |
| Rₜ | Unexplained descriptive remainder |
| Gθ | A learnable structure-generation strategy |
| Sₜ | The temporary executable structure |

Execution should return:

~~~text
Execute(Sₜ) → (result, failure traces, user corrections, new descriptive remainder)
~~~

Risk principle:

~~~text
Greater uncertainty + less reversible action → stronger need for user confirmation
~~~

Reversible exploration can be appropriate under uncertainty. Uncertainty does not authorize deleting files, publishing publicly, making payments, or using sensitive data in high-risk ways.

## 10. Comparison with conventional agents and recommenders

**Editorial note:** This is the source's intended design contrast. Existing systems vary; this table does not establish that every agent or recommender lacks the listed capabilities, or that MirrorMind has implemented them.

| Conventional pattern described in the source | Intended MirrorMind design |
| --- | --- |
| Complete tasks inside a fixed tool framework | Generate temporary tool structures from available capabilities |
| Optimize completion, clicks, or preference matching | Also consider task advancement, agency, and longer-term intention |
| Treat anomalies as error or noise | Use anomalies as an opportunity to reassess the model |
| Let the system primarily maintain user models | Make state representations visible, editable, and deletable |
| Converge on a stable profile | Retain remainder and allow users to exceed previous models |
| Adapt to observed behavior | Learn collaboration without prescribing purposes |

## 11. A minimal testable prototype

The first version does not need whole-computer scanning or a personal large model. MirrorReader could test this loop:

1. The user explicitly enters an intention and optional state.
2. Read the previous position, annotations, and unresolved questions.
3. Generate two reading structures, such as restoring context and examining an argument critically.
4. Show the reasons, assumptions, and uncertainty behind the proposal.
5. Let the user choose, modify, or reject it.
6. Save the structure, feedback, and whether the task continued.
7. Adjust recommendations in similar later contexts.
8. When behavior contradicts predictions, start a simplified reverse-state-identification process.

Minimum validation criteria:

- The same material produces different structures for different intentions or states.
- Users understand why information is organized that way.
- Corrections affect the next generation.
- The system can articulate what it does not know.
- Anomalies do not immediately become personality labels.
- The process still shortens the path into the task.

**Editorial note:** This is a proposed experiment. The current MirrorReader script implements paragraph navigation only.

## 12. Value boundaries

1. Learn how to help people realize intentions; leave the choice of intentions to them.
2. Do not equate actual human state with data or interpretations.
3. Allow change, anomalies, and restarting rather than fixing a person to historical patterns.
4. Preserve necessary friction for safety, reflection, and irreversible decisions.
5. Do not convert every remainder into a demand for more data; some things can remain unknown.
6. Do not make clicks, dwell time, or dependency the primary success metrics.
7. Let users inspect, revise, delete, and reset representations of themselves.

## 13. Open questions

1. How can meaningful anomalies be distinguished from ordinary noise or bad data?
2. What minimum state fields make the system operational without overdefining the person?
3. How can we tell whether a structure advances intention rather than merely feeling smooth?
4. When should the system propose a state hypothesis, and when should it remain silent?
5. How can raw remainder be retained alongside privacy, storage costs, and forgettability?
6. When should learning remain in rules and memory, and under what conditions should it reach model parameters?
7. How can exploratory structures distinguish hypotheses without manipulating users?

## 14. One-sentence definition

> Self-structuring acknowledges that human–environment states cannot be fully represented symbolically, compiles current intention, provisional state, personal history, environmental capabilities, and descriptive remainder into revisable temporary executable structures, and learns across time how to collaborate with that person.
