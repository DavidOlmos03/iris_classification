# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only the necessary files 
COPY pyproject.toml poetry.lock* ./

# Install only production dependencies
RUN poetry install --only main --no-root --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Run tests with Poetry
RUN poetry run pytest tests/ --disable-warnings

# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application with uvicorn using Poetry
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

