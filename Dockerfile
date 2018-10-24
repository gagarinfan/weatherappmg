FROM python:3

ADD . /

RUN pip install requests apscheduler
RUN echo "Europe/Berlin">/etc/timezone

CMD [ "python3", "-u", "app.py" ]
