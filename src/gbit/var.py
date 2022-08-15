from termcolor import colored

SUID = colored(f"SUID", 'yellow', attrs=['bold'])
SUDO = colored(f"SUDO", 'yellow', attrs=['bold'])
SHELL = colored(f"SHELL", 'yellow', attrs=['bold'])
File_Write = colored("File Write", 'yellow')
File_Read = colored("File Read", 'yellow')
etc_passwd = colored("/etc/passwd", 'red', attrs=['bold', 'dark'])
etc_shadow = colored("/etc/shadow", 'red', attrs=['bold', 'dark'])
file_to_read = colored("file_to_read", 'red')
file_to_write = colored("file_to_write", 'red')

line = colored("-------------", "red")