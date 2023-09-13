FROM ubuntu 
#RUN apt update 
#RUN apt install –y apache2 
#RUN apt install –y apache2-utils 
#RUN apt clean 
RUN apt update && \
    apt install -y apache2 && \
    apt install -y apache2-utils
EXPOSE 80
ENV WHEEL_VERSION=0.0.3

#CMD ["/bin/sleep", "100h"]
CMD ["apache2ctl","-D","FOREGROUND"]
