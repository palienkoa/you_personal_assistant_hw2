FROM python:3.12.0

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy project files
COPY . /app/

# Disable virtual environment creation and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

# Set the command to run the application
CMD ["python", "console_interface.py"]