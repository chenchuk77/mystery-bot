#!/bin/bash

# get version from Dockerfile
WHEEL_VERSION=$(grep 'WHEEL_VERSION' Dockerfile | cut -d "=" -f2)


#1. check screen res
#2. check dep ( ffmpeg )
#3. check/start web
#python3 mystery-bot


# starting wheel-server if necessary
X=$(docker ps | grep wheel)
if [[ $X = "" ]]; then
  echo "starting wheel-server (v-${WHEEL_VERSION})..."
  ./start-wheel-server.sh
  sleep 3s
fi

# starting bot
python3 mystery-bot.py




#
#
#
# then echo da; else echo nei, di
#> ^C
#chenchuk@chenchuk-work:~/dev/mystery-bot$ X=$(docker ps | grep wheel)
#chenchuk@chenchuk-work:~/dev/mystery-bot$ if [ $X = "" ];  then echo da; fi
#bash: [: =: unary operator expected
#chenchuk@chenchuk-work:~/dev/mystery-bot$
#chenchuk@chenchuk-work:~/dev/mystery-bot$ if [[ $X = "" ]]; then echo da; fi
#da
#chenchuk@chenchuk-work:~/dev/mystery-bot$ ./start-wheel-server.sh
#Error response from daemon: No such container: wheel-web-server
#Error: No such container: wheel-web-server
#c3d5604225c4d55480038dccf33950fca3f272162d71e1bbb23e9d62bad1a524
#chenchuk@chenchuk-work:~/dev/mystery-bot$
#chenchuk@chenchuk-work:~/dev/mystery-bot$ X=$(docker ps | grep wheel)
#chenchuk@chenchuk-work:~/dev/mystery-bot$ if [[ $X = "" ]]; then echo da; fi
#chenchuk@chenchuk-work:~/dev/mystery-bot$
