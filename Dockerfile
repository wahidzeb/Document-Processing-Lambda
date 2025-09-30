# Stage 1: Build the dependencies in a slim environment
FROM python:3.9-slim-buster as builder

# Set the working directory
WORKDIR /var/task

# Install build essentials that might be needed for some packages
RUN apt-get update && apt-get install -y build-essential

# Copy and install requirements
COPY lambda_function/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -t /var/task/packages

# Stage 2: Create the final Lambda image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory
WORKDIR /var/task

# Copy the installed packages from the builder stage
COPY --from=builder /var/task/packages ./packages

# Copy the Lambda function code
COPY lambda_function/app.py .

# Add the packages to the Python path
ENV PYTHONPATH=/var/task/packages

# Set the command to run the handler
CMD [ "app.lambda_handler" ]