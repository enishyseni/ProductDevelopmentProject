FROM nikolaik/python-nodejs:latest

RUN apt-get update
RUN apt-get install -y python python-pip python-dev 

COPY . .
RUN pip install -r requirements.txt
RUN npm install
RUN npm run build


EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]