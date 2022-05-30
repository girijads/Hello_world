FROM centos:7
RUN yum install -y python-setuptools sudo wget gcc gcc-c++ make openssl-devel python-devel libevent git python-pip bzip2-devel libffi-devel
RUN curl https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz --output Python-3.7.9.tgz
RUN tar xzf Python-3.7.9.tgz
RUN cd Python-3.7.9 && ./configure --enable-optimizations && make altinstall

ADD . /tmp/
WORKDIR /tmp
RUN pip3.7 install -r /tmp/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3.7" ]
CMD [ "app.py" ]
