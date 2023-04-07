from fastapi import Fastapi

app = Fastapi()

@app.get('/')
def help_check():
  return {"hello" : "world"}
