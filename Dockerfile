# Use a Python base image
FROM python:3.11-slim

# Install Rust toolchain (required by maturin)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install build dependencies
RUN apt-get update && apt-get install -y \
  build-essential \
  libssl-dev \
  libffi-dev \
  python-dev \
  git

# Set the working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Create a virtual environment
RUN python -m venv .venv
RUN .venv/bin/pip install --upgrade pip

# Install Python dependencies
RUN .venv/bin/pip install -r requirements.txt

# Set the entry point for the application
CMD [".venv/bin/python", "manage.py", "runserver"]
