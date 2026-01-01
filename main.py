from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.post('/pf_auth')
async def get_user(request: Request):
    body = await request.body()

    try:
        json_data = request.json()
        print("Auth JSON:", json_data)
    except Exception:
        print ("Raw Request:", body)

    print("Headers:", request.headers)

    return {"result": 1, "message": "Successfully sent authorization request"}

