from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True,log_level="debug")