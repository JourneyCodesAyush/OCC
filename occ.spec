# occ.spec
a = Analysis(
    ['src/occ/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['occ.config','importlib.metadata'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='occ',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon=None,
)