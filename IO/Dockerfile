FROM python:3.8.6-alpine3.11

WORKDIR /var/www/
ADD . /var/www/

RUN pip install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8082

CMD python app.py