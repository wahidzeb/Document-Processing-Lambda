# Document-Processing-Lambda
Repository to be use as AWS Lambda to get document from AWS S3 Bucker and Process using DocLing and AI and then update dynamodb with document information

## Packaging for Deployment

To deploy this function to AWS Lambda, you need to create a zip file that includes the function code and its dependencies.

1.  **Install dependencies:**

    Install the Python packages listed in `lambda_function/requirements.txt` into the `lambda_function` directory.

    ```bash
    pip install -r lambda_function/requirements.txt -t ./lambda_function
    ```

2.  **Create the zip file:**

    Navigate into the `lambda_function` directory and zip its contents.

    ```bash
    cd lambda_function
    zip -r ../lambda_function.zip .
    cd ..
    ```

3.  **Upload to Lambda:**

    Upload the `lambda_function.zip` file to your AWS Lambda function.
