FROM python:latest

RUN pip install requests bs4 cherrypy lxml
ADD fxserver-version.py ./
EXPOSE 8080
CMD ["python", "fxserver-version.py"]
