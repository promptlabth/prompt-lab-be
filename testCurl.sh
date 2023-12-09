curl -X 'POST' \
  'localhost:8000/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNhM2JkODk4ZGE1MGE4OWViOWUxY2YwYjdhN2VmZTM1OTNkNDEwNjgiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRW5kZXJtYW4yMSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKc2lVSHpLQUhaNk45Q051T0Z0X0dROUJ6LVdXaXNRbjZOUFJRWS1yamludk09czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJvbXB0LWxhYi0zODM0MDgiLCJhdWQiOiJwcm9tcHQtbGFiLTM4MzQwOCIsImF1dGhfdGltZSI6MTcwMjA5NTU3OCwidXNlcl9pZCI6Ik1WOUZKeVBwMTZVeWJmUXFTbkdGUk5nSDYxNzMiLCJzdWIiOiJNVjlGSnlQcDE2VXliZlFxU25HRlJOZ0g2MTczIiwiaWF0IjoxNzAyMDk1ODA3LCJleHAiOjE3MDIwOTk0MDcsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMDU5OTg1ODY5ODI5MDMxNjk2MzkiXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.MuPgjeg1xa50SwRNhy-3oIHm7XYoYJpuraJ8aAaMKxt7UYWxCgJpGK1Bow1Ocdc0Sgz8MmAOFm5ZV-ekyolNVwOPTBTTLA6wdEHBNSDbuPS28G70nhAKRE8y9kqhlvm7dx_dWRH3lVS9PsuXOmzfmJOcPj9NpW3LI7qHMpwxUHFD-9NDf33UDNUNZphMIOGL8KhcUlDnCs_6RQxONWnoFJ4ljchNqFuP81Kmk7CczHCQ1MvOSY37ZEjJvj-XWPWnNov5xJiJoUeeMFmA1Zf2iUjcU7s6XHxYgcOWlX3trtJrvlZ-US1UPfUuC9NxNWOzBGiciWryiXW9HKiKbM_Fdg" \
  -d '{
  "platform": "string",
  "access_token": "string"
}'

# curl -X 'POST' \
#   'localhost:8000/users/login' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -H "Authorization: Bearer a" \
#   -d '{
#   "platform": "string",
#   "access_token": "string"
# }'