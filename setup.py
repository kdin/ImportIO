from distutils.core import setup
import py2exe

setup(
	options = {'py2exe':{'bundle_files':1}},
	console = ['ImportIO-DA-Extension.py'],
	zipfile = None,
	)