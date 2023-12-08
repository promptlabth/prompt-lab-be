curl -X 'POST' \
  'localhost:8000/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
  "platform": "string",
  "access_token": "string"
}'