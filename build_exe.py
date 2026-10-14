import platform
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


PROJECT = Path(__file__).resolve().parent
DIST = PROJECT / "dist"
APP = DIST / "Class Clash"
ARCHIVE = DIST / "Class-Clash-Windows-x64.zip"


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

    if not (APP / "Class Clash.exe").is_file():
        raise FileNotFoundError(f"The EXE was not created: {APP / 'Class Clash.exe'}")

    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as archive:
        for file_path in APP.rglob("*"):
            if file_path.is_file():
                relative_path = file_path.relative_to(APP)
                if relative_path.parts[0] in {"saves", "crash_logs", "update"}:
                    continue
                if relative_path.name == "update.zip":
                    continue
                archive.write(
                    file_path,
                    file_path.relative_to(DIST),
                )

    print(f"Build complete: {ARCHIVE}")


if __name__ == "__main__":
    main()
