# ADR-0002: Human-Triggered Document-to-Spec Automation

## Status

Accepted for phased implementation

## Context

New PDFs, emails, spreadsheets, Word files, slides and images may arrive after
a project has started. Manually rebuilding product specifications each time is
slow and error-prone.

The enterprise environment is air-gapped. Raw documents must remain local.

## Decision

Build a human-triggered local document-to-spec workflow.

### Initial Flow

1. Place new files into `input/inbox`.
2. Human explicitly triggers processing.
3. System hashes files and identifies new or changed evidence.
4. Docling and format-specific fallback extractors parse files locally.
5. Local models draft proposed changes to specifications.
6. System generates a Git diff and a review summary.
7. Human approves or rejects the proposed specification changes.
8. Only approved specifications become inputs for development.

## Future Automation Levels

### Level 1: Deterministic Script

A Bash or Python script runs after a human command.

### Level 2: Internal Interface

A human clicks a button in a small internal application.

### Level 3: Agent Skill

Hermes Agent or another constrained agent invokes the deterministic script
after an explicit human request.

### Level 4: Durable Enterprise Workflow

Use a durable workflow engine, policy controls, logging and human approval
checkpoints.

## Control Principle

Agents may draft and recommend.
Agents must not silently approve their own specification changes.

## Air-Gap Position

- Use local parsing.
- Use local model inference.
- Retain raw evidence locally.
- Review licences before importing model weights or dependencies.
- Maintain an offline package and model import process.
