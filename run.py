import os, platform


os.system("git pull")

bit = platform.architecture()[0]
if "32bit" in bit:
    from dump_32 import Login
    Login()
elif "64bit" in bit:
    from dump_64 import Login
    Login()
else:
    print("[×] Sorry your device is not support")