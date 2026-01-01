from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/pf_authen')
async def get_authen(request: Request):
    body = await request.body()

    try:
        json_data = request.json()
        print("Auth JSON:", json_data)
    except Exception:
        print ("Raw Request:", body)

    print("Headers:", request.headers)

    return {"result": 1, "message": "Successfully sent authorization request"}

@app.post('/pf_author')
async def get_author(request: Request):
    body = await request.body()
    try:
        json_data = request.json()
        print("Auth JSON:", json_data)
    except Exception:
        print("Raw Request:", body)

    print("Headers:", request.headers)

    return {"access_duration":"1H","access_level":"guest","sponsor":1 ,"unregdate":"2030-01-01","category":"default"}
