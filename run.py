import os, platform


os.system("git pull")
bit = platform.architecture()[0]
if "64bit" in bit:
    from dump_64 import Login
    Login()
