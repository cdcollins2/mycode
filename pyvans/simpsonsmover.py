#!/usr/bin/env python3
import paramiko

paramiko.util.log_to_file('/tmp/paramiko.log')

hosts = ["10.10.2.3", "10.10.2.4", "10.10.2.5"]
users = ["bender", "fry", "zoidberg"]
port = 22
passw = "alta3"

for host, user in zip(hosts, users):
    transport = paramiko.Transport((host, port))
    transport.connect(username = user, password = passw)

    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.put("simpsons-ans.txt", "simpsons-ans.txt")
    sftp.put("simpsons-py.txt", "simpsons-py.txt")

    sftp.close()
    transport.close()
