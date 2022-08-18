from gbit.var import *

gtfobin = f"""
{SHELL}
{line}
{colored("It can be used to break out from restricted environments by spawning an interactive system shell.", 'blue')}
{colored("    env /bin/sh", 'green')}

{SUID}
{line}
{colored("If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to", 'blue')}
{colored("access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to", 'blue')}
{colored("run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default sh", 'blue')}
{colored("shell to run with SUID privileges.", 'blue')}

{colored("This example creates a local SUID copy of the binary and runs it to maintain elevated privileges. To", 'blue')}
{colored("interact with an existing SUID binary skip the first command and run the program using its original", 'blue')}
{colored("path.", 'blue')}
{colored("    sudo install -m =xs $(which env) .", 'green')}
{colored("    ./env /bin/sh -p", 'green')}

{SUDO}
{line}
{colored("If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and", 'blue')}
{colored("may be used to access the file system, escalate or maintain privileged access.", 'blue')}
{colored("   sudo env /bin/sh", 'green')}
"""