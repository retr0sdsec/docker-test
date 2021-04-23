FROM ubuntu

RUN apt -y update \
	&& apt -y install software-properties-common \
	&& add-apt-repository ppa:deadsnakes/ppa \
	&& apt -y update \
	&& apt -y install python3.8 \
	&& apt -y install python3-pip \
	&& pip3 install aiogram \
	&& pip3 install bs4

VOLUME /home/docker/bot_parse/

WORKDIR /home/docker/bot_parse/

COPY ./ /home/docker/bot_parse/

CMD python3 bot.py 
