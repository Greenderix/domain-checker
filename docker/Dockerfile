# Use the official Python image as a base image
FROM python:3.10

# Set the working directory within the container
WORKDIR /app

# Install uvicorn and dependencies
RUN pip install uvicorn[standard] gunicorn

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
