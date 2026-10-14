import platform
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


PROJECT = Path(__file__).resolve().parent
DIST = PROJECT / "dist"
ARCHIVE = DIST / "Class-Clash-Windows-x64.zip"
EXE = DIST / "Class Clash.exe"


def main():
    if (
        sys.implementation.name != "cpython"
        or sys.version_info[:2] != (3, 15)
        or platform.architecture()[0] != "64bit"
        or sys.platform != "win32"
    ):
        raise RuntimeError(
            "Build Class Clash with 64-bit CPython 3.15 on Windows."
        )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            str(PROJECT / "requirements-build.txt"),
        ],
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--noconfirm",
            "--clean",
            str(PROJECT / "Class Clash.spec"),
        ],
        cwd=PROJECT,
        check=True,
    )

    if not EXE.is_file():
        raise FileNotFoundError(f"The EXE was not created: {EXE}")

    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.write(EXE, EXE.name)

    print(f"Build complete: {ARCHIVE}")


if __name__ == "__main__":
    main()
