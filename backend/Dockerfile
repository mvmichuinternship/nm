# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /the_bot

# Copy the requirements.txt file to the container
COPY requirements.txt .

RUN apt-get update && apt-get install -y gcc

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port that the Flask app will run on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]
