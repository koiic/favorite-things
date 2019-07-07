#!/usr/bin/env bash

echo "start docker build ========"
docker-compose -f Docker/docker-release/docker-compose.yml build --no-cache

echo " end docker build ============= build successful ======================="

echo " start docker instance  ==================="
docker-compose -f Docker/docker-release/docker-compose.yml up

echo " docker instanc running successfully "

cd app/client && npm install --verbose
echo " dependencies installed successfully"



echo "Script run successfully"
