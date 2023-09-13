#!/bin/bash

# get version from Dockerfile
WHEEL_VERSION=$(grep 'WHEEL_VERSION' Dockerfile | cut -d "=" -f2)

docker stop wheel-web-server || true
docker rm wheel-web-server || true


docker run -d --rm --name wheel-web-server \
    -v ${PWD}/js/examples/basic_code_wheel:/var/www/html \
    -e SERVER_TYPE=WHEEL \
    -e TEST=FAKE \
    -p 8282:80 wheel-web-server:${WHEEL_VERSION}



    #-v ${PWD}/js/examples/basic_code_wheel:/usr/local/apache2/htdocs \
#i/var/www/html
