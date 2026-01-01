from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/Start')
async def start_auth(request: Request):
    body = await request.body()

    try:
        json_data = request.json()
        print("Auth JSON:", json_data)
    except Exception:
        print ("Raw Request:", body)

    print("Headers:", request.headers)

    return {"result": ["OK"]}

@app.post('/Stop')
async def stop_dummy():
    return {"result": ["OK"]}

