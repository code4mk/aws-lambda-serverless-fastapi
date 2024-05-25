# aws-lambda-serverless-fastapi
Deploy fastapi on aws lambda with serverless

* production ready
* good project structure
* cd/cd with github action

# local development (fastapi)

## env
```bash
# create virtual environment
python3 -m venv .aws_lambda_fastapi_venv

# activate virtual environment
source .aws_lambda_fastapi_venv/bin/activate
```

## run fast api project

```bash
# install packages
pip3 install -r requirements.txt

# run project with uvicorn
uvicorn "fastapi_project.main:app" --reload --port=8000
```

# deploy on production

## github action 

set secrets `SERVERLESS_ACCESS_KEY` , `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

## serverless
* set your data

```bash
# serverless.yml
org: code4mk
app: demo-app-api-fastapi
service: demo-app-api-fastapi
```

## with cli

```bash
 serverless deploy --aws-profile your_aws_profile_name 
```



