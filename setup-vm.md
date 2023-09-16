
### to setup vm :
1. download ubuntu 22.04 from: https://www.linuxvmimages.com/images/ubuntu-2204/
2. download virtualbox from: https://www.virtualbox.org/wiki/Downloads
3. create vm: virtualbox: machine -> add -> ubuntu.vbox 
4. login with ubuntu:ubuntu (for root: sudo su -)

```bash
cd ~/Downloads
sudo apt-get update 
sudo apt install -y git curl vim python3-pip ffmpeg vlc
CHROME_VERSION=114.0.5735.198-1
wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
sudo dpkg -i ./google-chrome-stable_${CHROME_VERSION}_amd64.deb
cd ..
git clone https://github.com/chenchuk77/mystery-bot.git
cd mystery-bot
pip install -r requirements.txt


install docker and post install
restart vm

./build-wheel-image.sh

```
6. 
7. 
8. 
9. 
   cd ~/Downloads
   wget http://archive.ubuntu.com/ubuntu/pool/universe/f/ffmpeg/ffmpeg_4.2.7-0ubuntu0.1_amd64.deb
   sudo dpkg -i ffmpeg_4.2.7-0ubuntu0.1_amd64.deb
   wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb

6. 
7. 
8. 
9. 
10. 
   sudo snap install ffmpeg (4.3.0: tested on 4.2.7-0ubuntu0.1)
   sudo snap install vlc
   git clone https://github.com/chenchuk77/mystery-bot.git
   install chrome: https://www.cyberithub.com/how-to-install-google-chrome-on-ubuntu-22-04-lts-jammy-jellyfish/

   CHROME_VERSION=114.0.5735.198-1
   wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb



install docker: https://docs.docker.com/engine/install/ubuntu/
   sudo usermod -aG docker $USER

6. restart vm (for nonroot user to manage docker)

7. start wheel-web-server
   cd mystery-bot
   ./build-wheel-image.sh
   ./start-web-server.sh
   docker ps

8. install python dependencies
   cd mystery-bot
   pip install -r requirements.txt
   create credentials.py file

9. change vm display settings to 1920x1080







5. install python 3.8.10 (no need python 3.10 installed)

ffmpeg version 4.2.7-0ubuntu0.1 Copyright (c) 2000-2022 the FFmpeg developers



install ffmpeg v4.2.7 from source ( ~10 minutes to compile )
git clone https://git.ffmpeg.org/ffmpeg.git
git checkout 55a95339526ba3ad6c3c31721ab1ecfd957eb5b4  # v4.2.7
cd ffmpeg
./configure --prefix=/usr --extra-version=0ubuntu0.1 --toolchain=hardened --libdir=/usr/lib/x86_64-linux-gnu --incdir=/usr/include/x86_64-linux-gnu --arch=amd64 --enable-gpl --disable-stripping --enable-avresample --disable-filter=resample --enable-avisynth --enable-gnutls --enable-ladspa --enable-libaom --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcdio --enable-libcodec2 --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libjack --enable-libmp3lame --enable-libmysofa --enable-libopenjpeg --enable-libopenmpt --enable-libopus --enable-libpulse --enable-librsvg --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx265 --enable-libxml2 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-lv2 --enable-omx --enable-openal --enable-opencl --enable-opengl --enable-sdl2 --enable-libdc1394 --enable-libdrm --enable-libiec61883 --enable-nvenc --enable-chromaprint --enable-frei0r --enable-libx264 --enable-shared

make
sudo make install
sudo reboot



