FROM python:3.7.4-slim

ENV CLASS1_ENABLED=1
ENV CLASS3_ENABLED=0
ENV CLASSES=class1,class3

COPY main.py main.py
COPY classes classes

CMD [ "python", "main.py" ]