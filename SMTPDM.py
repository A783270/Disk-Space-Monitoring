import paramiko
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

key = paramiko.RSAKey.from_private_key_file("Location Of Keys", password = "")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
client.connect( hostname = "", port = "",username = "" ,pkey = key )
print("connected")

commands = ["df -h" ]
for command in commands:
    print("Hello")
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    usage = stdout.read().decode().split()
    err = stderr.read().decode()
    if err:
        print(err)
Threshold = int(usage.strip('%'))
if Threshold > 90 :
        print("Disk Space Running out")
else:
        print("Mail Process")
        msg = MIMEMultipart()
        msg['From'] = ''
        msg['To'] = ''
        msg['Subject'] = 'SMTP Mail'
        body = 'Testing Purpose Body Mail'
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('SMTP server', 25)  ### put your relevant SMTP here
        #server.login('from@domain.com', 'password_here')  ### if applicable
        server.send_message(msg)
        server.quit()

