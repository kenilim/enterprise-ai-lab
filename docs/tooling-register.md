# Enterprise AI Development Lab: Tooling Register

## Guiding Principle

Except for OpenAI models used temporarily to accelerate personal development,
prefer open-source components that can be installed and operated inside an
air-gapped enterprise environment.

Open-weight models must still undergo licence review before enterprise use.

## Tool Classification

| Component | Lab Role | Classification | Air-Gap Position | Notes |
|---|---|---|---|---|
| OpenCode | Coding-agent interface | OSS | Candidate | Supports multiple providers and local models |
| Docling | Document ingestion | OSS, MIT | Candidate | Parse PDFs, DOCX, PPTX, XLSX, images and other formats |
| OpenSpec | Spec-driven workflow | OSS, MIT | Candidate | Disable telemetry in enterprise configuration |
| Ollama | Local inference runner | Local-lab tool | Evaluate | Convenient for workstation experiments |
| qwen3:14b | Local text model | Open-weight model | Review required | Used for local text experiments |
| qwen3-vl:8b | Local vision model | Open-weight model | Review required | Used for visual-content experiments |
| Python | Scripting runtime | OSS | Candidate | Local orchestration and fallback extraction |
| pandas | Tabular processing | OSS | Candidate | Excel and CSV analysis |
| openpyxl | XLSX processing | OSS | Candidate | Spreadsheet-specific fallback extractor |
| python-docx | DOCX processing | OSS | Candidate | Office-document fallback extractor |
| python-pptx | PPTX processing | OSS | Candidate | Slide-content fallback extractor |
| OpenAI models | Coding accelerator | Proprietary exception | Replace | Personal lab only |
| ChatGPT OAuth plugin | OpenCode authentication | Personal-lab exception | Replace | Do not use for enterprise deployment |
| Docker Desktop | Workstation container tooling | Personal-lab convenience | Replace or review | Use approved enterprise container runtime |
| WSL2 | Windows workstation Linux layer | Personal-lab convenience | Replace | Use approved Linux infrastructure |

## Review Fields for Future Tools

For every new tool, record:

- Source repository
- Licence
- Version
- Purpose
- Offline installation method
- Required model weights
- Required package mirrors
- Telemetry behaviour and opt-out setting
- Security considerations
- Enterprise replacement, if any
