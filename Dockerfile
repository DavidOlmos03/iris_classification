# Base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy all files to the working directory
COPY . .

# Install dependencies and run tests in one RUN step
RUN pip install --no-cache-dir -r requirements.txt && \
    pytest tests/ --disable-warnings


# Expose port 8000 for the application
EXPOSE 8000

# Command to run the application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
