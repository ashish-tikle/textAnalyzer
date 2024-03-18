# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python files into the container
COPY . .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose any ports if needed
# EXPOSE 8080

# Command to run the Python script
CMD ["python", "main.py"]
