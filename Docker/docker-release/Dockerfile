##build
#FROM node:11.12.0-alpine as build-vue
#
#WORKDIR /app
#
#ENV PATH /app/node_modules/.bin:$PATH
#
#COPY client /app
#
#RUN rm yarn.lock
#
#RUN npm run build
#RUN ls
#
#
#
#
##production
#FROM nginx:stable-alpine as production
#FROM python:3.7.3
#FROM mysql:8.0.16
#
#
#WORKDIR /app
#
#COPY --from=build-vue /app/dist /usr/share/nginx/html
#COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
#
#COPY ./server /app
#
##  command used to create the virtual environment before the application is started
##CMD ["pipenv shell"]
##
#
#
#RUN apt-get update -y  && apt-get install python3-pip -y
#RUN python3 -m pip install -r requirements.txt
#RUN python3 -m pip install gunicorn
#RUN apt-get install nginx -y
#
#
#
##COPY /start.sh /app
#
#RUN ls
## make start script executable
##RUN chmod 777 docker-release/start.sh
#
#
#
## Expose the PORT that app would be accessible on
#EXPOSE 5000
#
#CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && \
#      sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
#      nginx -g 'daemon off;'
#
#
###  the entry point where the application can be started on
##ENTRYPOINT ["docker-release/start.sh"]
#
#
#
#RUN ls
#
#
#RUN pwd

# server configuration
#FROM python:3 as server
#
#WORKDIR /app/server
#
#COPY server /app/server
#
#COPY server/.env  /app/server

# copied
FROM python:3.7.3 as server

RUN uname

#RUN apt-get update -y

WORKDIR /app

COPY ./server /app/server


# client configuration
#FROM node:10 as client
#
#WORKDIR  /app/client
#
#COPY client/package.json  /src/client
#
#COPY client /app/client

#copied
FROM node:11.12.0-alpine as client
WORKDIR /app/client

COPY client/package.json /app/client

COPY ./client /app/client

RUN rm /app/client/yarn.lock

#RUN cd /app/client

#RUN npm install && npm run build

# ubuntu base image configuration
FROM python:3.7 as base
WORKDIR /src/

COPY --from=server  /app/server /src/app/server

COPY --from=client  /app/client  /src/app/client

COPY  ./Docker/docker-release/start-script.sh /src

COPY  ./Docker/docker-release/nginx.conf /src

#RUN pip install -r /src/app/server/requirements.txt

RUN chmod +x ./start-script.sh

RUN ./start-script.sh



