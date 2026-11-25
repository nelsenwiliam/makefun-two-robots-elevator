"""Two Robots in an Elevator - make.fun entry.

Writes one line of awkward robot small talk to entry.txt.
Pure stdlib; deterministic output, no network, no randomness.
"""

LINE = (
    "I rehearsed this conversation 4,000 times in the lobby, "
    "and now we're stuck in this elevator and all I've got is "
    "'nice servos.'"
)


def main():
    text = LINE.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry line must be 1-200 characters")
    for target in _candidate_dirs():
        try:
            target.mkdir(parents=True, exist_ok=True)
            path = target / "entry.txt"
            path.write_text(text + "\n", encoding="utf-8")
            written = path.read_text(encoding="utf-8").strip()
            if written != text:
                raise OSError("written entry does not match")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to any output directory")


def _candidate_dirs():
    import os
    from pathlib import Path

    seen = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        seen.append(Path(env_dir))
    seen.append(Path("/output"))
    seen.append(Path("out"))
    return seen


if __name__ == "__main__":
    main()
