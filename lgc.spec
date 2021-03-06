# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['./lgc/__init__.py'],
             pathex=['./lgc/'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['matplotlib', 'tkinter', 'PySide2', 'pygame', 'PyQt5'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='lgc',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=['x86_64-linux-gnu', 'Win-x86_64'],
          codesign_identity='Nurul-GC',
          entitlements_file=None,
          icon='./lgc/lgc-icons/favicon-256x256.ico',
          version_file='./lgc/versionfile.txt' )
