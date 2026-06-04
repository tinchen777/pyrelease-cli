# -*- coding: utf-8 -*-
# Python version: 3.9
# @TianZhen

import argparse
import glob
import os
import shutil
import subprocess
import sys

from . import __version__


def clean():
    """Backup old distributions."""

    print("==> Cleaning")

    os.makedirs("history", exist_ok=True)

    # backup old dist files
    for f in glob.glob("dist/*"):
        dst = os.path.join("history", os.path.basename(f))
        if os.path.exists(dst):
            os.remove(dst)
        shutil.move(f, dst)

    # remove build cache
    # shutil.rmtree("build", ignore_errors=True)

    # # remove egg-info
    # for d in glob.glob("*.egg-info"):
    #     shutil.rmtree(d, ignore_errors=True)


def build():
    """Build package."""

    print("==> Building package")

    subprocess.run(
        [sys.executable, "-m", "build"],
        check=True,
    )


def upload():
    """Upload package to PyPI."""

    print("==> Uploading to PyPI")

    files = glob.glob("dist/*")

    if not files:
        raise RuntimeError("No distribution files found.")

    try:
        subprocess.run(
            [sys.executable, "-m", "twine", "upload", *files],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error uploading: {e}")
        sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(
        prog="pyrelease",
        description="Build and publish Python packages.",
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "--clean", "-c",
        action="store_true",
        help="Only clean build cache.",
    )

    parser.add_argument(
        "--build-only", "-bo",
        action="store_true",
        help="Clean and build, but do not upload.",
    )

    parser.add_argument(
        "--upload-only", "-uo",
        action="store_true",
        help="Upload existing dist/ files.",
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.clean:
        clean()

    elif args.build_only:
        clean()
        build()

    elif args.upload_only:
        upload()

    else:
        clean()
        build()
        upload()

    print("==> Done!")


if __name__ == "__main__":
    main()
