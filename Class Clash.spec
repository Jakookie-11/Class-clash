# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.win32.versioninfo import (
    FixedFileInfo,
    StringFileInfo,
    StringStruct,
    StringTable,
    VarFileInfo,
    VarStruct,
    VSVersionInfo,
)


project = Path(SPECPATH)
datas = []
version_string = (project / "version.txt").read_text(encoding="utf-8").strip()
version_numbers = tuple(
    int(part)
    for part in version_string.split("-", 1)[0].split(".")
)
version_numbers = (version_numbers + (0, 0, 0, 0))[:4]

for directory in ("musik", "Down_in_Mars"):
    source = project / directory
    if not source.is_dir():
        raise FileNotFoundError(f"Required game assets are missing: {source}")
    datas.append((str(source), directory))

for filename in (
    "standard.json",
    "version.txt",
    "README.md",
    "README.pdf",
    "More info.md",
    "More info.pdf",
    "Class Clash – Installation unter Windows.md",
    "Class Clash – Installation unter Windows.pdf",
):
    source = project / filename
    if not source.is_file():
        raise FileNotFoundError(f"Required game file is missing: {source}")
    datas.append((str(source), "."))

a = Analysis(
    [str(project / "main.py")],
    pathex=[str(project)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="Class Clash",
    icon=str(project / "class_clash.ico"),
    version=VSVersionInfo(
        ffi=FixedFileInfo(filevers=version_numbers, prodvers=version_numbers),
        kids=[
            StringFileInfo(
                [
                    StringTable(
                        "040904B0",
                        [
                            StringStruct("CompanyName", "Jakob Samstag"),
                            StringStruct("FileDescription", "Class Clash"),
                            StringStruct("FileVersion", version_string),
                            StringStruct("InternalName", "Class Clash"),
                            StringStruct("OriginalFilename", "Class Clash.exe"),
                            StringStruct("ProductName", "Class Clash"),
                            StringStruct("ProductVersion", version_string),
                        ],
                    )
                ]
            ),
            VarFileInfo([VarStruct("Translation", [1033, 1200])]),
        ],
    ),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
)
