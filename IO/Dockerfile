FROM python:3.8.6-alpine3.11

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/
ADD . /var/www/

RUN pip install -r requirements.txt

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

COPY . /usr/src/app/

EXPOSE 8082

CMD python app.py