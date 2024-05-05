# Use an official Python image as a base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . .
# Copy the requirements file
COPY pyproject.toml .

RUN poetry install

# Install the dependencies
#RUN pip install --no-cache-dir -r requirements.txt



# Expose the port the application will use
#EXPOSE 8000

# Run the command to start the application when the container starts
CMD ["python", "console_interface.py"]