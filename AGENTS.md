# Agent installation entrypoint

This repository distributes proposal-producer 0.2.0-trial as a standalone Python installer containing the complete Skill ZIP and per-file hashes.

When the user requests installation, read README.md, clone this repository or download install.py, and run it with an available Python 3 runtime. The default is ~/.agents/skills/proposal-producer; --project or --dest selects another location. An identical repeat is unchanged; --update preserves the previous installation outside discovery directories.

After extraction, read SKILL.md. JSON contracts contain fields, thresholds, enums and checklists; schemas validate data; executable gates bind confirmation and review evidence to actual artifacts. Install requirements.txt in the task's Python environment if needed, then run the validate command. Do not silently change global packages or host permissions.

Report the actual installation path and version. Check document generation, PDF rendering and CJK fonts separately. Hook adapters require host registration; installation alone does not enable them. Installation does not request creation or external delivery of client proposals.
