from gbit.var import *

gtfobin = f"""
{Command}
{line}
{colored("It can be used to break out from restricted environments by running non-interactive system", 'blue')}
{colored("commands.", 'blue')}
{colored("The commands are executed according to the crontab file edited via the crontab utility.", 'blue')}
{colored("   crontab -e", 'green')}

{SUDO}
{line}
{colored("If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and", 'blue')}
{colored("may be used to access the file system, escalate or maintain privileged access.", 'blue')}
{colored("The commands are executed according to the crontab file edited via the crontab utility.", 'blue')}
{colored("    sudo crontab -e", 'green')}
"""