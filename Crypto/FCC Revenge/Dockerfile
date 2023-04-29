FROM python:3.10-alpine

RUN apk add socat

WORKDIR /app

RUN pip install pip
RUN pip install timezones
RUN pip install pycryptodome
ENV TZ="Asia/Ho_Chi_Minh"

ENV PORT 3002
ENV FILE_NAME chal.py

COPY $FILE_NAME .
COPY flag.txt .

CMD socat -T20 -dd -v -v TCP-LISTEN:$PORT,reuseaddr,fork EXEC:'python3 '$FILE_NAME',pty,stderr,setsid,sigint,sane'
