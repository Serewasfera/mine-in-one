print("Starting Mine-In-One 1.0 by Serewasfera...")

import minecraft_launcher_lib, subprocess, sys, os

if os.path.exists("game"):
    pass
else:
    os.mkdir("game")
if sys.argv[1] == minecraft_launcher_lib.utils.get_installed_versions("game")[0]["id"]:
    pass
else:
    print(f"Installing version {sys.argv[1]}...")
    minecraft_launcher_lib.install.install_minecraft_version(sys.argv[1], "game")
    
if minecraft_launcher_lib.runtime.get_executable_path("java-runtime-alpha", "game") != None:
    pass
else:
    print("Installing JVM runtime...")
    minecraft_launcher_lib.runtime.install_jvm_runtime("java-runtime-alpha", "game")
    
options = {
    "username": sys.argv[2],
    "uuid": "0",
    "token": "",
    "executablePath": minecraft_launcher_lib.runtime.get_executable_path("java-runtime-alpha", "game"),
    "launcherName": "MineInOne",
    "launcherVersion": "1.0",
    "gameDirectory": "game",
}

print("Creating a game process...")
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(sys.argv[1], options['gameDirectory'], options))