FROM python:2.7.15

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install -y nodejs

COPY . .
RUN pip install -r requirements.txt
RUN npm install
RUN npm run build

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]