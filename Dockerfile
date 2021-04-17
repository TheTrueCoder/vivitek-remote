FROM python:alpine
COPY src/requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY src/ /app
CMD [ "python", "/app/test.py" ]