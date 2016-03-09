FROM ubuntu@sha256:0844055d30c0cad5ac58097597a94640b0102f47d6fa972c94b7c129d87a44b7
#Ubuntu 14.04
MAINTAINER Vict  Tan <ychtan@email.gwu.edu>

#This pre-fetches the most recent requirements.apt in dev.
ADD https://raw.githubusercontent.com/gwu-libraries/sfm-weibo-datasts/master/requirements/requirements.apt /opt/setup/
RUN apt-get update
RUN cat /opt/setup/requirements.apt | tr "\n" " " | xargs apt-get install -y
RUN pip install pip==7.1.2

ADD https://github.com/gwu-libraries/sfm-weibo-datasts/archive/master.zip /opt/setup/
RUN unzip master.zip
RUN mv sfm-weibo-datasts-master /opt/sfm-weibo-datasts

#This pre-fetches the most recent requirements.txt.
RUN pip install -r /opt/sfm-weibo-datasts/requirements/master.txt --upgrade

#Install appdeps to allow checking for application dependencies
RUN pip install appdeps

#This is used to automatically create the admin user.
RUN pip install django-finalware==0.1.0

ADD invoke.sh /opt/
RUN chmod +x /opt/invoke.sh

WORKDIR /opt/sfm-weibo-datasts
CMD ["/opt/invoke.sh"]
EXPOSE 80