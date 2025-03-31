from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(
    name="JungleWar",
    version="1.0",
    description="Jungle War app",
    options={"build.exe": {"packages": ["pygame"]}},
    executables=executables

)