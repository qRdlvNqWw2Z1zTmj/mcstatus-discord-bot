FROM resin/rpi-raspbian:stretch 

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install discord.py mcstatus

ADD bot.py /
ADD token.txt /

CMD [ "python3", "./bot.py" ]
