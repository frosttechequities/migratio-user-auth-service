# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# Using --no-cache-dir to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
# This includes main.py, models.py, supabase_client.py, etc.
COPY . .

# Expose the port the app runs on (e.g., 8002 for this service)
# Render will set the PORT environment variable, and Uvicorn can use it.
# We'll use 8002 as a default if PORT is not set by the environment.
EXPOSE 8002

# Command to run the application using Uvicorn
# The command should be `uvicorn main:app --host 0.0.0.0 --port ${PORT:-8002}`
# Render sets the PORT environment variable.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
