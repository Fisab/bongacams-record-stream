from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ['idna', 'livestreamer', 'json', 'requests']
options = {
	'build_exe': {
		'packages':packages,
	},

}

setup(
	name = 'bongacams-record',
	options = options,
	version = "0.1",
	description = 'bongacams stream record',
	executables = executables
)
