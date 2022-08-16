from termcolor import colored

SUID = colored(f"SUID", 'yellow', attrs=['bold'])
SUDO = colored(f"SUDO", 'yellow', attrs=['bold'])
SHELL = colored(f"SHELL", 'yellow', attrs=['bold'])
Reverse_shell = colored("Reverse Shell", 'yellow', attrs=['bold'])
File_upload = colored("File upload", 'yellow', attrs=['bold'])
File_download = colored("File Download", 'yellow', attrs=['bold'])
File_write = colored("File Write", 'yellow', attrs=['bold'])
File_read = colored("File Read", 'yellow', attrs=['bold'])
Library_load = colored("Library load", 'yellow', attrs=['bold'])
line = colored("-------------", "red", attrs=['bold'])

etc_passwd = colored("/etc/passwd", 'red')
etc_shadow = colored("/etc/shadow", 'red')
File_Write = colored("File Write", 'yellow')
File_Read = colored("File Read", 'yellow')
file_to_read = colored("file_to_read", 'red')
file_to_write = colored("file_to_write", 'red')
file_to_send = colored("file_to_send", "red")
file_to_get = colored("file_to_get", "red")
file_to_save = colored('file_to_save', "red")

backslash = "{chr(92)}"
opening_curly_braces =  "{chr(123)}"
closing_curly_braces = "{chr(125)}"