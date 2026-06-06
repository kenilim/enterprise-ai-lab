# ADR-0001: Open-Source-First Architecture with Dual Model Routing

## Status

Accepted

## Context

The personal lab is intended to teach an enterprise-style AI development
workflow that can later be reproduced inside an air-gapped environment.

The personal workstation can access OpenAI models, but the enterprise
environment cannot.

## Decision

Use two model routes:

### Route A: Local Evidence and Specification Route

- Parse unstructured documents locally
- Use local open-source or open-weight tools and models
- Preserve evidence and source references locally
- Draft requirements, design and task specifications locally
- Require human review before development

### Route B: Personal-Lab Development Route

- Send approved, synthetic or sanitised specifications to OpenCode
- Use OpenAI coding models temporarily to accelerate development
- Do not send confidential workplace documents or sensitive raw evidence
- Replace this route with an internal coding model in the enterprise design

## Consequences

### Benefits

- Sensitive evidence stays local
- The workflow is transferable to an air-gapped environment
- Cloud models accelerate hands-on learning
- The cloud dependency is isolated and replaceable

### Limitations

- The personal lab is not identical to the enterprise deployment
- Local model licences require review
- OpenAI usage must remain limited to approved synthetic or sanitised content
