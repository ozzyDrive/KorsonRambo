# Korson Rambo Discord Bot

## Local development
* Bot token (Ossilta)
* Python 3
* ffmpeg
* Python libraries:
  * `pip install discord.py[voice]`
  * `pip install youtube_dl`

## Docker
* Insert bot token into Dockerfile CMD's last parameter
* Build the image
  * `docker build -t korsonrambo .`
* Run the container
  * `docker run korsonrambo`
  * Use `-d` flag for detached container