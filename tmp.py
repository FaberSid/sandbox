import os
import getpass
import pwd

print(os.getlogin())
print(getpass.getuser())
print(os.environ.get("USER"))
print(pwd.getpwuid(os.getuid())[0])