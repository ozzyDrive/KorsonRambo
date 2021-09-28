FROM python:3

ADD main.py /
ADD YTDLSource.py /

RUN apt-get update
RUN apt-get install libopus0

COPY --from=mwader/static-ffmpeg:4.1.4-2 /ffmpeg /ffprobe /usr/local/bin/

RUN pip install discord.py[voice]
RUN pip install youtube_dl

CMD [ "python", "./main.py" , "<BOT TOKEN HERE>"]