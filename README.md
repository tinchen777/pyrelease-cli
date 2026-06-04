<div align="center">

<h2 id="title">
🐱‍👓 pyrelease-cli 🐱‍👓<br>
<sub>Automate Your Python Package Release Workflow</sub>
</h2>

[![PyPI version](https://img.shields.io/pypi/v/pyrelease-cli.svg)](https://pypi.org/project/pyrelease-cli/)
![Python](https://img.shields.io/pypi/pyversions/pyrelease-cli?color=brightgreen)
![License](https://img.shields.io/github/license/tinchen777/pyrelease-cli.svg)

![Github stars](https://img.shields.io/github/stars/tinchen777/pyrelease-cli.svg)

</div>

## About

`pyrelease-cli` is a simple CLI tool for building and publishing Python packages.

- Python: 3.8+

## Installation

### Install from PyPI

This installs the core package with minimal dependencies.

```bash
pip install pyrelease-cli
```

## Quick Start

Before using it, make sure your project contains a valid `pyproject.toml` and that you have configured your PyPI credentials.

### Publish a package

```bash
pyrelease
```

This command will:

1. Create the `history/` directory if it does not exist.
2. Move existing files in `dist/` to `history/`.
3. Remove build cache (`*.egg-info/`).
4. Build the package using: `python -m build`
5. Upload all generated distributions to PyPI using: `python -m twine upload dist/*`

---

### Build only

Build the package without uploading it.

```bash
pyrelease --build-only
```

This will:

* Clean previous build artifacts.
* Build the package.
* Keep the generated files in `dist/`.

---

### Upload only

Upload existing distribution files in `dist/`.

```bash
pyrelease --upload-only
```

This is useful when a previous upload failed and you do not want to rebuild the package.

---

### Clean build artifacts

Remove build cache and archive old distributions without building or uploading.

```bash
pyrelease --clean
```

---


## Requirements

- Python >= 3.8
- `build`
- `twine`
- A valid `pyproject.toml`
- PyPI credentials configured for `twine`

## License

See LICENSE in the repository.

## Links

- [Homepage/Repo](https://github.com/tinchen777/pyrelease-cli.git)
- [Issues](https://github.com/tinchen777/pyrelease-cli.git/issues)
