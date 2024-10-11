from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# "static"ディレクトリをホスティング
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "FastAPI server is running. Go to /static to view your files."}
