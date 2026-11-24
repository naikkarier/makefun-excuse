import os

LINE = "My clock synced to a server that still thinks it is Tuesday, so in my defence the deadline has not happened yet."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, "line must be 1 to 160 characters, got %d" % len(text)
    assert "\n" not in text, "line must be a single line"
    assert "\r" not in text, "line must not contain a carriage return"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
