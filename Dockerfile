FROM python:3

ADD main.py /
ADD YTDLSource.py /

RUN apt-get update
RUN apt-get install libopus0

COPY --from=mwader/static-ffmpeg:4.1.4-2 /ffmpeg /ffprobe /usr/local/bin/

RUN mv /usr/local/bin/ffmpeg /usr/local/bin/ffmpeg.exe 

RUN pip install discord.py[voice]
RUN pip install youtube_dl

CMD [ "python", "./main.py" , "ODkxMDgyOTUyNzI4MDE0OTE5.YU5Lqw.WeynBWyhDlX3cntSTqjyxWJLsCk"]