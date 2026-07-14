# Prompt objects

Store each prompt as:

```text
prompts/<prompt-slug>/<semantic-version>/
├── PROMPT.md
├── MANIFEST.json
└── NOTES.md              # optional; interpretation, not evidence
```

## Rules

- `PROMPT.md` contains the exact reusable prompt text.
- `MANIFEST.json` identifies state, provenance, intended use, claims, limitations, and the SHA-256 of `PROMPT.md`.
- Once a version is `LOCKED`, never edit its bytes. Create a successor version.
- Keep experiment outputs outside the prompt directory so prompt identity is stable.
- Do not embed secrets, private transcripts, hidden system prompts, or model-generated claims presented as facts.
- A prompt may be `CANDIDATE` or `LOCKED` without being `DEMONSTRATED`.

## Naming

Use lowercase kebab-case slugs and semantic versions such as `v0.1.0`. Version changes describe artifact identity, not quality.
