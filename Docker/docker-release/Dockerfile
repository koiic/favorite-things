#build
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



