FROM python:2-onbuild
MAINTAINER james@lshift.net

ENV SLACK_TOKEN="xxx"
ENV WORKABLE_TOKEN="yyy"

CMD [ "python", "./rtmbot.py" ]
