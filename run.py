import os, platform


os.system("git pull")

bit = platform.architecture()[0]
if "32bit" in bit:
    import dump
    dump.Login()
elif "64bit" in bit:
    import dumpb
    dumpb.Login()
else:
    print("[×] Sorry your device is not support")
