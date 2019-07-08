#!/usr/bin/env bash

echo "start docker build ========"
docker-compose -f Docker/docker-release/docker-compose.yml build --no-cache

echo " end docker build ============= build successful ======================="

echo " start docker instance  ==================="
docker-compose -f Docker/docker-release/docker-compose.yml up

echo " docker instance running successfully "


echo "Script run successfully"
