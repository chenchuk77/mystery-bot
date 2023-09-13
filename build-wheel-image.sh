#!/bin/bash -e

#
# this script builds wheel-web-server image
# it does not push it, use it for dev only

# get version from Dockerfile
WHEEL_VERSION=$(grep 'WHEEL_VERSION' Dockerfile | cut -d "=" -f2)

echo "building local image wheel-web-server:${WHEEL_VERSION} ..."
sleep 2s

echo "building the current workspace ..."
docker build -t wheel-web-server:${WHEEL_VERSION} .
sleep 2s

echo "done."
echo ""

