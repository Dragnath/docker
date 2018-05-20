import requests
import os
from paramiko_sshd import setSSH, host_ip, container_id
import settings as st


class TestClass:
    def test_SSH(self):
        connection = setSSH(host_ip, st.username, st.password, st.port)
        process = connection.execute_remote_command(st.command_process)
        hostname = connection.execute_remote_command(st.command_hostname)
        assert bool(process) is True and hostname == container_id

    def test_HTTP_response(self):
        r = requests.get(st.url)
        books = r.json()
        num_of_books = len([element['ID'] for element in books])

        for enum, book in enumerate(books, 1):
            r = requests.get(st.url + '/%s' % enum, params={'ID': enum})
            assert r.status_code == 200
        assert num_of_books == len(books)

    def test_SCP(self):
        connection = setSSH(host_ip, st.username, st.password, st.port)
        filename = os.path.basename(st.excel_sheet)
        file = connection.execute_remote_command('ls | grep %s' % filename)

        package = st.command_install.split()[-1]
        package_code = connection.execute_remote_command(st.command_check.format(package))
        if package_code != '0':
            connection.execute_remote_command(st.command_install)
        connection.set_scp(st.localpath, st.remotepath)
        assert str(file) == str(filename)
