# paramiko_sshd.py variables
username = 'root'
password = 'admin123'
port = '2001'
command_process = 'ps ax | grep [/]usr/sbin/sshd'
command_hostname = "echo ${HOSTNAME}"
command_container = "docker container ps | grep _sshd | awk '{print $1}'"

# move_file.py
command_install = "yum install -y openssh-clients"
command_check = 'yum list installed {} > /dev/null ; echo $?'
localpath = '../resources/Books.xlsx'
remotepath = '/root'
ip_url = "http://localhost/user"

# api.py variables
url = 'http://localhost/book'

# excel_books.py variables
excel_sheet = 'resources/Books.xlsx'