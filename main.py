# app/main.py
from fastapi import FastAPI
from router import router  # Import your router module

app = FastAPI()

# Register the router into the main app instance
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the main application!"}
