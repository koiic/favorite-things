#!/usr/bin/env bash

# install python requirement
pip install -r app/server/requirements.txt

# Install Node Js
{
    apt-get update -y
    apt-get install curl --yes
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    # load nvm
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
    # load nvm bash_completion
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
    nvm install 11.14
    echo "Nodejs Installed successful"
} || {
        echo "Installation failed for nodejs"
}

#install dependencies from package.json
cd app/client && npm install --verbose
echo " dependencies installed successfully"

#run build
npm run build
echo " npm run build"

ls

#Installing nginx
echo " Installing nginx"
apt-get install nginx --yes
echo " Installation complete"


cd ../..

echo "copy nginx.conf file"
cp nginx.conf  /etc/nginx/nginx.conf

echo "Script run successfully"
