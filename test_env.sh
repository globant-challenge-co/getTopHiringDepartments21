aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 118846062185.dkr.ecr.us-east-1.amazonaws.com
docker build -t get-top-dept-hiring-21-container-test .
docker tag get-top-dept-hiring-21-container-test:latest 118846062185.dkr.ecr.us-east-1.amazonaws.com/get-top-dept-hiring-21-container-test:latest
docker push 118846062185.dkr.ecr.us-east-1.amazonaws.com/get-top-dept-hiring-21-container-test:latest