FROM python:latest
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD python3 bot.py