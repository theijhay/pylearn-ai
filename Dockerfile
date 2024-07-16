FROM python:3.12-slim

# Install build tools
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-dev && \
    apt-get install -y gcc

# Install the required packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your application code
COPY . /app
WORKDIR /app

CMD ["python", "app.py"]
