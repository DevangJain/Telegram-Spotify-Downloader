# by @mastermindvrtx

FROM jrottenberg/ffmpeg:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip python3-dev
RUN python -m pip install --upgrade pip
RUN apt-get instal npm
RUN git clone https://github.com/DevangJain/Telegram-Spotify-Downloader && \
    cd Telegram-Spotify-Downloader
    pip3 install -U -r requirements.txt
RUN npm install -g spotify-dl

WORKDIR /Telegram-Spotify-Downloader
CMD python3 bot.py
