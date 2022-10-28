FROM python
RUN apt-get -y update
RUN apt-get -y install vim # Docker

RUN mkdir -p /project/server
ADD . /project/server
WORKDIR /project/server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]