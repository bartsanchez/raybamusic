FROM node:14
RUN npm install -g @angular/cli
COPY raybamusic /tmp/raybamusic
WORKDIR /tmp/raybamusic
RUN npm install
CMD ng serve --open --host 0.0.0.0