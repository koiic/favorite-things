#!/usr/bin/env bash

# install python requirement
pip install -r app/server/requirements.txt

BOLD='\e[1m'
GREEN='\e[92m'
NC='\e[0m'
RED='\e[31m'
YELLOW='\e[33m'

function installNodeJS() {
    if [[ ! $(which node) ]]; then
        apt-get update -y
        apt-get install curl --yes
        curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
        export NVM_DIR="$HOME/.nvm"
        # load nvm
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        # load nvm bash_completion
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
        nvm install 11.14
        printf "\n${BOLD}${GREEN} Nodejs Installed successful ${NC} \n"
    else
        printf "\n${BOLD}${YELLOW} NodeJS already exist ${NC} \n"
    fi
}


function installYarn() {
    printf "\n${BOLD}${GREEN} installing yarn ${NC} \n"
    curl -o- -L https://yarnpkg.com/install.sh | bash
    export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
}

function setupApplication() {
    cd app/client
    yarn install
    yarn run build
    printf "\n${BOLD}${GREEN} dependencies installed successfully ${NC} \n"
}

function installAndConfigureNginx() {
  printf "\n${BOLD}${GREEN} Installing nginx ${NC} \n"
  apt-get install nginx -y
  printf "\n${BOLD}${GREEN} Installation complete ${NC} \n"
  cd ../..
  printf "\n${BOLD}${GREEN} copying nginx.conf file ${NC} \n"
  cp nginx.conf  /etc/nginx/nginx.conf
  printf "\n${BOLD}${GREEN} Script run successfully ${NC} \n"
}

main () {
  installNodeJS
  installYarn
  setupApplication
  installAndConfigureNginx
}

main

