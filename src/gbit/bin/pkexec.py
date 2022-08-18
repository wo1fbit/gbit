from gbit.var import *

gtfobin = f"""
{SUDO}
{line}
{colored("If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and", 'blue')}
{colored("may be used to access the file system, escalate or maintain privileged access.", 'blue')}
{colored("    sudo pkexec /bin/sh", 'green')}
"""