FROM python

ENV USER_ID            1000
ENV GROUP_ID           1000
ENV USER_GROUP_NAME    docker

RUN apt-get update && apt-get install -y \
    vim \
    sudo

RUN groupadd -g $GROUP_ID $USER_GROUP_NAME
RUN useradd -u $USER_ID -g $GROUP_ID -m $USER_GROUP_NAME

RUN mkdir -p /home/docker/pyvenv
RUN python3 -m venv /home/docker/pyvenv
RUN /home/docker/pyvenv/bin/python3 -m pip install --upgrade pip
RUN /home/docker/pyvenv/bin/pip3 install schedule
RUN /home/docker/pyvenv/bin/pip3 install pylast


RUN mkdir -p /home/docker/docker
RUN chown -R $USER_GROUP_NAME:$USER_GROUP_NAME /home/docker/docker
RUN chmod -R 777 /home/docker/docker

