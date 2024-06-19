FROM python:3.11
EXPOSE 5000
WORKDIR /app
RUN pip3 install Flask 
COPY . . 
#copies curr directory into the image
CMD ['flask', 'run', "--host", "0.0.0.0"]
