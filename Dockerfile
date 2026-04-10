# use official python image as the base image
FROM python:3.9-slim

#Set the working directory in the container
WORKDIR /app
# copy the requirements file into the container
COPY requirements.txt .
# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# copy the rest of the application code into the container
COPY . .
#Rub the application on port 5000
CMD ["python", "app.py"]