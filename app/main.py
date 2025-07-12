from fastapi import FastAPI
from app.scan_engine import run_scan

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DeploySure-AI is running"}

@app.get("/scan")
def scan_cloud():
    result = run_scan()
    return {"scan_result": result}