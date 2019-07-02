#build
FROM node:11.12.0-alpine as build-vue

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY client /app

RUN rm yarn.lock

RUN npm run build
RUN ls




#production
FROM nginx:stable-alpine as production
FROM python:3.7.3
FROM mysql:8.0.16


WORKDIR /app

COPY --from=build-vue /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

COPY ./server /app

#  command used to create the virtual environment before the application is started
#CMD ["pipenv shell"]
#


RUN apt-get update -y  && apt-get install python3-pip -y
RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install gunicorn
RUN apt-get install nginx -y



#COPY /start.sh /app

RUN ls
# make start script executable
#RUN chmod 777 docker-release/start.sh



# Expose the PORT that app would be accessible on
EXPOSE 5000

CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && \
      sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
      nginx -g 'daemon off;'


##  the entry point where the application can be started on
#ENTRYPOINT ["docker-release/start.sh"]



RUN ls


RUN pwd
