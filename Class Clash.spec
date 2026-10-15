# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path


project = Path(SPECPATH)
datas = []

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

    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
)
