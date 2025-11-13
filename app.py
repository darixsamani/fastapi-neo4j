from database.database import initiate_database
from routes.posts import  PostRouter
from routes.users import  UserRouter
from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    initiate_database()
    yield
    # You can also close DB connections here if needed
    print("App shutdown complete.")

app = FastAPI(lifespan=lifespan, description="Template for building FastAPI applications with Neo4j.", contact={"email": "samanidarix@gmail.com", "tel": "691439424"})


FORMAT = '%(levelname)s: %(asctime)-15s: %(filename)s: %(funcName)s: %(module)s: %(message)s'
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, format=FORMAT)




@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(UserRouter, tags=["Administrator"], prefix="/users")
app.include_router(PostRouter, tags=["Posts"], prefix="/posts",)