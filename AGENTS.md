# Agent installation entrypoint

This repository distributes proposal-producer 0.1.0-trial as a standalone Python installer containing the complete Skill ZIP and file hashes.

When the user requests installation, read README.md, clone this repository or download install.py, and run it with an available Python 3 runtime. The default is ~/.agents/skills/proposal-producer; --project or --dest selects other locations. The installer verifies the embedded archive and all 18 files. An identical repeat is unchanged; --update preserves the previous installation outside discovery directories.

Report the actual path and version. Check the host's document generation, PDF export/rendering and Chinese fonts separately; the installer does not install these engines. The install request does not request creation or external delivery of client proposals.
