import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if "64bit" in bit:
    from File_64_enc import main
    main()
else:
    print("[×] Sorry your device is not support")
