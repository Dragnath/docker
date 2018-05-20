import paramiko
import socket
from scp import SCPClient
import subprocess as sp
import settings as st


class setSSH:
    def __init__(self, host, username, password, port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def setup_ssh(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(username=self.username, hostname=self.host,
                    password=self.password, port=self.port)
        return ssh

    def execute_remote_command(self, command):
        ssh = self.setup_ssh()
        stdin, stdout, stderr = ssh.exec_command(command)
        output_lines = stdout.read().strip()
        ssh.close()
        return output_lines

    def set_scp(self, localpath, remotepath):
        ssh = self.setup_ssh()
        scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
        scpclient.put(localpath, remotepath)
        ssh.close()


host_ip = socket.gethostbyname(socket.gethostname())
container_id = sp.check_output(st.command_container, shell=True, stdin=sp.PIPE).strip()
