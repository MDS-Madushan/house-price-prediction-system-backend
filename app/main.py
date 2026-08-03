from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Template",
    description="A simple FastAPI template",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message":"this is the root of house price prediction API"}

@app.get("/health")
def read_health():
    return {"status":"ok"}