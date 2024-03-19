from cx_Freeze import setup, Executable
import sys
build_exe_options = {
        'packages' : ['random', 'pygame', 'sys'],
        'include_files' : ['fon.jpg', 'icon.jpg', 'lead.jpg', 'NeutralFace.otf', 'player.jpg', 'text.otf']
}
base = None
iconi = 'icon.ico'
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
        name = "Mafia",
        version = "1",
        description = "the typical 'Hello, world!' script",
        options = {'build_exe': build_exe_options},
        executables = [Executable("Mafia.py", base=base, icon=iconi)])
