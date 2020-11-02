import paramiko

key = paramiko.RSAKey.from_private_key_file("location of the file", password = "")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
client.connect( hostname = "", port = "",username = "" ,pkey = k )
print("connected")

commands = ["ls" ]
for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    usage = stdout.read().decode()
    err = stderr.read().decode()
    if err:
        print(err)
print(usage)

