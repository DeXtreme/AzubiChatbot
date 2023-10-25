# Use python image
FROM python:3.10-alpine

# Create app directory
WORKDIR /app

# Install requirements
ADD requirements.txt ./
RUN pip install -r requirements.txt

# Start app
ADD /src/* ./
ENTRYPOINT [ "python", "chatbot.py" ]
