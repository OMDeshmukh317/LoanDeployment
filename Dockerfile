# Use a Python base image with Rust pre-installed
ENV CARGO_HOME=/app/.cargo

FROM rust:1.70-slim AS builder

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install Python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Run the application
CMD ["python3", "manage.py", "runserver"]
