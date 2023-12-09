# broze account
curl -X 'GET' \
  'localhost:8000/remaining-message' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNhM2JkODk4ZGE1MGE4OWViOWUxY2YwYjdhN2VmZTM1OTNkNDEwNjgiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVGhhbmF3dXQgVHVhbXByYWphayIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQWNIVHRkc1RZNFhlMFo0eGJhQ1hhazhIWEtRMkkzTjJEZ3pZRmV5M2dNRk5ZV1Y9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJvbXB0LWxhYi0zODM0MDgiLCJhdWQiOiJwcm9tcHQtbGFiLTM4MzQwOCIsImF1dGhfdGltZSI6MTcwMjEzNDI0NSwidXNlcl9pZCI6IklycGVHWjIyOEtNTTN4MzF2RDN2ZmV0SXpGWTIiLCJzdWIiOiJJcnBlR1oyMjhLTU0zeDMxdkQzdmZldEl6RlkyIiwiaWF0IjoxNzAyMTM0MjUwLCJleHAiOjE3MDIxMzc4NTAsImVtYWlsIjoiYjYzMDIyNDVAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMDQwNDU1NDk1ODI1MDA2NDkxNjUiXSwiZW1haWwiOlsiYjYzMDIyNDVAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.RgKrRzkPCXjfRIKkQyzYWLA7R2P_0py2Ejb6EcAphIznNOvHHK8pWK4QF4xAz6w3jmVYf0bCbxc5hhZJVJCiNi9ByPInXqm-d119OT8dC80MC4uA6AGwcz50PH_97PqrC88SMG9df6NzlAQ_K3VJ2mnKPhqbfYUAFBYJFojQ-BJGOJj33Z3-JqmjwkFuqGIK0A6_uYquDcSDGasIrATnn-OAjiFq14CkAlxuZuEZ5djjmnLtD94iXSnPWsHW7LejWh1wDosG0Z_vngLly7u_bj0Z-TrgkMxNtMQXrVd80sJYWyhjYKul_zCQ6Kan5GZ2YMqdHXdAM5_5kjc3sJ1Zew" \
  -d '{
  "platform": "gmail",
  "access_token":"ya29.a0AfB_byAoI6h5tdEKd4U56Gus8GWv7hbFY6E3Gr5oKDHujMATlQDW8fYifLY3MBao8bl-CUQe4IuP6MnFwsieZYoxmQ0fChz23uMBDxwpQqlV62aa3xZZ8Yiek0_BVhSV-_XdcodLJDbePkIP13RAvJ_9jzkxA5e7W97uE-rram0aCgYKAdASARMSFQHGX2MiKcyA1mg0cBHXeNCdER705g0178"
}'

# # free account
# curl -X 'POST' \
#   'localhost:8000/users/login' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjNhM2JkODk4ZGE1MGE4OWViOWUxY2YwYjdhN2VmZTM1OTNkNDEwNjgiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRW5kZXJtYW4yMSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKc2lVSHpLQUhaNk45Q051T0Z0X0dROUJ6LVdXaXNRbjZOUFJRWS1yamludk09czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJvbXB0LWxhYi0zODM0MDgiLCJhdWQiOiJwcm9tcHQtbGFiLTM4MzQwOCIsImF1dGhfdGltZSI6MTcwMjA5NTU3OCwidXNlcl9pZCI6Ik1WOUZKeVBwMTZVeWJmUXFTbkdGUk5nSDYxNzMiLCJzdWIiOiJNVjlGSnlQcDE2VXliZlFxU25HRlJOZ0g2MTczIiwiaWF0IjoxNzAyMDk1ODA3LCJleHAiOjE3MDIwOTk0MDcsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMDU5OTg1ODY5ODI5MDMxNjk2MzkiXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.MuPgjeg1xa50SwRNhy-3oIHm7XYoYJpuraJ8aAaMKxt7UYWxCgJpGK1Bow1Ocdc0Sgz8MmAOFm5ZV-ekyolNVwOPTBTTLA6wdEHBNSDbuPS28G70nhAKRE8y9kqhlvm7dx_dWRH3lVS9PsuXOmzfmJOcPj9NpW3LI7qHMpwxUHFD-9NDf33UDNUNZphMIOGL8KhcUlDnCs_6RQxONWnoFJ4ljchNqFuP81Kmk7CczHCQ1MvOSY37ZEjJvj-XWPWnNov5xJiJoUeeMFmA1Zf2iUjcU7s6XHxYgcOWlX3trtJrvlZ-US1UPfUuC9NxNWOzBGiciWryiXW9HKiKbM_Fdg" \
#   -d '{
#   "platform": "string",
#   "access_token": "string"
# }'

# # test
# curl -X 'POST' \
#   'localhost:8000/users/login' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -H "Authorization: Bearer a" \
#   -d '{
#   "platform": "string",
#   "access_token": "string"
# }'