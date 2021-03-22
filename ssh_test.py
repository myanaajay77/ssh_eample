import paramiko

user_name = 'ubuntu'
pass_word = 'ubuntu'
host_name = '3.86.77.173'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname = host_name,username = user_name,password = pass_word,key_filename = 'Downloads/Jenkins_trail.pem')
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.readlines())
ssh.close()