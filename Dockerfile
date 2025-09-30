# Use the official AWS Lambda Python runtime as a base image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory in the container
WORKDIR /var/task

# Copy the requirements file into the container
COPY lambda_function/requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Lambda function code into the container
COPY lambda_function/app.py .

# Set the CMD to your handler (could be wrong if your file is not named app.py or your function is not named lambda_handler)
CMD [ "app.lambda_handler" ]