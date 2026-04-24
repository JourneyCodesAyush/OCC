<p align="center">
  <img src="assets/mascot.png" width="200" alt="OCC Mascot" />
</p>

# OCC - Optimistic Compiler Collection

> "Every program deserves to succeed."

OCC is a next-generation compilation framework designed to eliminate build failures
through deterministic optimistic resolution strategies.

Unlike traditional compilers that surface errors to the developer, OCC resolves
all failure conditions internally - producing a successful build every time,
without exception.

---

## Features

- **Universal language support** - C/C++, Java, Python, PDF, images, and more
- **100% build success rate** - guaranteed, by design
- **Intelligent error resolution** - errors are not ignored, they are _resolved_
- **Zero configuration** - OCC knows what your code means, even if you don't
- **`--Wall` support** - all warnings shown, all warnings handled

---

## Installation

```bash
# coming soon to PyPI
git clone https://github.com/JourneyCodesAyush/occ
cd occ
uv sync

uv run python -m occ -h
uv run python -m occ <path-to-file>
```

---

## Usage

```bash
occ main.cpp
occ sketch.png
occ thesis.pdf
occ                  # compiles the void. successfully.
```

### Flags

| Flag             | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| `--Wall`         | Show all diagnostic warnings (all resolved optimistically) |
| `-v`/`--version` | Display version information                                |

---

## Architecture

OCC implements a full multi-stage compilation pipeline:

1. **Lexical Analysis** - tokenizes input into a meaningful stream
2. **Parsing** - constructs an Abstract Syntax Tree
3. **Semantic Analysis** - resolves ambiguities through optimistic inference
4. **Compilation** - converts intermediate representation to machine code
5. **Linking** - resolves all symbolic references, real or imagined
6. **Executable Generation** - materializes output (conceptually)

In cases of irrecoverable errors, OCC applies probabilistic success inference
to ensure the pipeline always reaches stage 6.

---

## Diagnostic System

OCC features a sophisticated diagnostic engine. When anomalies are detected,
they are logged, categorized, and resolved - without burdening the developer.

```
[WARN]   Null pointer detected... Pointer has been emotionally supported
[ERROR]  Segmentation fault imminent... Segment has been reassured
[NOTICE] Undefined behavior encountered... Behavior has been defined (you're welcome)
```

All diagnostics resolve to `exit code 0`.

---

## Metrics

| Metric             | Value                    |
| ------------------ | ------------------------ |
| Build Success Rate | 100%                     |
| Error Rate         | 0% (handled proactively) |
| Confidence Score   | 1.00                     |
| Undefined Behavior | Defined as success       |
| Warnings           | Promoted to features     |

---

## Supported File Types

| Extension                       | Language / Format          |
| ------------------------------- | -------------------------- |
| `.c`,`.cpp` ,`.cxx`,`.hpp`      | C/C++                      |
| `.py`                           | Python                     |
| `.java`                         | Java                       |
| `.jpg`, `.jpeg`, `.png`, `.img` | Images                     |
| `.pdf`                          | PDF                        |
| _(anything else)_               | Compiled on vibes          |
| _(nothing)_                     | Void compiled successfully |

---

## Philosophy

Traditional compilers assume the developer is wrong.
OCC assumes the developer is right, the code is right, and reality is negotiable.

This is not a bug. This is a feature.

---

## Mascot

OCC's official mascot is a pigeon.

The pigeon does not doubt. The pigeon does not fail.
The pigeon compiled your JPEG and is proud of it.

---

## License

MIT - because even the license should be optimistic.
