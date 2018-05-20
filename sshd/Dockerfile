FROM centos

RUN yum -y update
RUN yum -y install openssh-server vsftpd
RUN ssh-keygen -A

ADD ./sshd_config /etc/ssh/sshd_config

RUN echo root:admin123 | chpasswd

CMD /usr/sbin/sshd -D
