# Approved Synthetic Product Brief: Spec Review Board MVP

## 1. Purpose

Build a small browser-based application that allows a product manager to
review user stories generated from unstructured source documents before those
stories are passed to a coding agent for implementation.

This is a synthetic learning exercise.

The application will not contain confidential workplace information.

## 2. Product-Development Context

The wider target workflow is:

`unstructured evidence → local extraction → locally drafted specifications → human review → approved user stories → coding agent → tests → deployment`

This MVP covers the human-review checkpoint.

## 3. Primary User

A product manager reviewing proposed user stories before approving development.

## 4. Core User Problem

AI-generated user stories may be incomplete, ambiguous or unsupported by the
source evidence.

The product manager needs a simple interface to:

- inspect each proposed story
- see its linked evidence references
- review its acceptance criteria
- approve it
- reject it
- request clarification
- filter the review queue by status

## 5. MVP Scope

### In Scope

- Browser-based application
- Responsive layout usable on desktop and mobile browser
- Seeded synthetic review items stored locally
- Review-queue page
- Story-detail view
- Linked source references displayed as text
- Acceptance criteria displayed for each story
- Review-status changes:
  - Pending
  - Approved
  - Rejected
  - Needs Clarification
- Reviewer note
- Review timestamp
- Filter by status
- Automated tests
- Local Docker execution

### Out of Scope

- User login
- Role-based access control
- External database
- File upload
- PDF parsing
- OCR
- Real AI-model calls
- Email ingestion
- Enterprise integrations
- Internet deployment
- Multi-user concurrency

## 6. Seed Data

Create at least four synthetic user stories.

Each seeded story must contain:

- story ID
- title
- user-story statement
- source-reference list
- acceptance-criteria list
- status
- reviewer note
- review timestamp

Use synthetic source references such as:

- `SYNTH-PDF-001 page 3`
- `SYNTH-EMAIL-002 paragraph 4`
- `SYNTH-XLSX-003 sheet Requirements row 12`
- `SYNTH-PPTX-004 slide 6`

## 7. Required User Stories

### STORY-001: View Review Queue

As a product manager, I want to view a list of proposed user stories so that I
can identify which items still require review.

#### Acceptance Criteria

- The queue displays all seeded stories.
- Each item displays its story ID, title and current status.
- The queue is readable on desktop and mobile browser widths.

### STORY-002: Inspect Story Details

As a product manager, I want to inspect a proposed story's evidence references
and acceptance criteria so that I can judge whether it is sufficiently
supported before development begins.

#### Acceptance Criteria

- Selecting a queue item opens or displays its details.
- Details include the user-story statement.
- Details include all linked source references.
- Details include all acceptance criteria.
- Details include the current reviewer note and review timestamp where present.

### STORY-003: Record Review Decision

As a product manager, I want to approve, reject or request clarification on a
story so that only sufficiently defined work proceeds to development.

#### Acceptance Criteria

- The reviewer can select Approved, Rejected or Needs Clarification.
- A reviewer note can be entered.
- Saving the decision updates the displayed status.
- Saving the decision records a timestamp.
- The saved result remains visible after refreshing the browser.

### STORY-004: Filter Review Queue

As a product manager, I want to filter the review queue by status so that I can
focus on pending or unresolved items.

#### Acceptance Criteria

- The queue can be filtered by status.
- An All option displays every story.
- The selected filter remains visibly active.
- The filtered story count is displayed.

## 8. Technical Constraints

- Use a lightweight web stack.
- Keep dependencies minimal.
- Store MVP data locally in the browser unless the approved design provides a
  strong reason to use another local-only approach.
- Include a Dockerfile.
- Include clear local-run instructions.
- Include automated tests.
- Do not introduce a backend unless justified in the design and approved by the
  human reviewer.

## 9. Test-Driven Development Rules

- Every user story must map to acceptance criteria.
- Every acceptance criterion must map to at least one automated test or an
  explicit documented manual test where automation is unreasonable.
- Write or update tests as part of implementation.
- Run the relevant tests after implementing each bounded story.
- If a test fails, determine whether the issue is:
  - an implementation defect
  - an incorrect test
  - an ambiguous requirement
  - a design mismatch
- Do not silently weaken a test merely to make the build pass.
- If a requirement changes, revisit the design, tasks and tests before
  continuing.

## 10. Agent Operating Rules

- Do not write application code during the proposal stage.
- Generate a proposal, requirements, design and task plan first.
- Keep each implementation task bounded and traceable to a story ID.
- Identify assumptions explicitly.
- Ask for human approval before implementation.
- Do not add features outside the MVP scope without approval.

## 11. Definition of Done

The MVP is complete only when:

- all four required user stories are implemented
- automated tests pass
- Docker build succeeds
- the application runs locally in Docker
- the human reviewer inspects the result
- the approved specifications and tasks are archived appropriately
