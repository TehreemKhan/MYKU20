import os
import subprocess

# os.system("date")
# subprocess.run(["ls","-l"])
# subprocess.run(["ls","-l","insulin.json"])


# command="uname"
# commandArgument="-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])