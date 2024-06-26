# aws-lambda-serverless-fastapi
Deploy fastapi on aws lambda with serverless

* production ready
* good project structure
* cd/cd with github action

# local development (fastapi)

## python virtual env
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

# or, run bash with shell
./run_fastapi_project.sh
```

# deploy on production

## github action 

* set secrets `SERVERLESS_ACCESS_KEY` , `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

NB: you can set environment variable `DATABASE_URL` and `LOAD_SQL_PROJECT` on lamda configuration (Environment variables). LOAD_SQL_PROJECT value will be `yes` 

## serverless

* set your own data

```bash
# serverless.yml
org: ****
app: demo-app-api-fastapi
service: demo-app-api-fastapi
```

## with cli

```bash
 serverless deploy --aws-profile your_aws_profile_name 
```


# project route

```bash
http://localhost:8000/api/v1/users
http://localhost:8000/health
```
