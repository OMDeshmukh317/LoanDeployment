# Use Rust base image for Rust tooling
FROM rust:1.70-slim as builder

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install Python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Set writable CARGO_HOME
ENV CARGO_HOME=/app/.cargo

# Run the application
CMD ["python3", "manage.py", "runserver"]
