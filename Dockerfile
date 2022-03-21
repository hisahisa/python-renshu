#FROM python:3.9.3-slim
#
#ENV PROJECT_HOME /home/circleci/project
#
## install aws cli
#RUN pip install awscli aws-mfa --upgrade
#
#COPY . ${PROJECT_HOME}
## install python test lib
#RUN pip install -r ${PROJECT_HOME}/requirements_test.txt
#
## install serverless
#RUN apt-get update
#RUN apt-get install -y sudo
#
##RUN apt-get update -y \
##    && apt-get upgrade -y \
##    && apt-get autoremove -y \
##    && apt-get install -y software-properties-common \
##    && add-apt-repository ppa:git-core/ppa \
##    && apt-get update -y
##
##RUN apt-get install -y git
#
## RUN apt-get install -y jq
#RUN sudo apt-get update && \
#    sudo apt-get install -y curl nodejs npm \
#    sudo npm install n -g && \
#    sudo n 14.17.0 && \
#    sudo apt purge -y nodejs npm && \
#    sudo npm i -g serverless@1.83.3 && \
#    sudo chmod +x /usr/local/bin/sls
#
## install node modules
#RUN sudo npm install --prefix ${PROJECT_HOME}
#
#RUN echo "circleci:x:300:" >> /etc/group \
#    && useradd -u 300 circleci -g 300
#
#RUN chown -R circleci:circleci /home/circleci
#USER circleci
#WORKDIR ${PROJECT_HOME}


From cimg/python:3.10.2

ENV PROJECT_HOME /home/circleci/project

# install aws cli
RUN pip install awscli aws-mfa --upgrade

COPY . ${PROJECT_HOME}
# install python test lib
RUN pip install -r ${PROJECT_HOME}/requirements_test.txt

# install serverless
RUN sudo apt-get update && \
    sudo apt-get install -y curl nodejs npm && \
    sudo npm install n -g && \
    sudo n 14.17.0 && \
    sudo apt purge -y nodejs npm && \
    sudo npm i -g serverless@1.83.3 && \
    sudo chmod +x /usr/local/bin/sls

# install node modules
RUN sudo npm install --prefix ${PROJECT_HOME}