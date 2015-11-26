# -*- mode: python -*-
a = Analysis(['ImportIO-DA-Extension.py'],
             pathex=['C:\\Users\\KD\\Desktop\\DA Extensions\\ImportIO'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ImportIO-DA-Extension.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
