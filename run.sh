docker build -t backend-ms-generate-prompt .
docker run -p 8080:8080 -e OPENAI_KEY=$OPENAI_KEY \
-e DB_USER=$DB_USER \
-e DB_PASSWORD=$DB_PASSWORD \
-e DB_HOST=$DB_HOST \
-e DB_PORT=$DB_PORT \
-e DB_NAME=$DB_NAME backend-ms-generate-prompt