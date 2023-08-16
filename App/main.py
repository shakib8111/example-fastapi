from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .Routers import post, user, auth, vote
from .config import settings


# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

# while True:
#     try:
#         conn = psycopg2.connect(host= "localhost", dbname="fastapi", user="postgres",
#                                password="stl8130", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to data base was failed")
#         print("Error: ", error)
#         time.sleep(2)
#
#
# def find_post(id):
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
#     # cursor.fetchone()
#     for p in my_posts:
#         if p["id"] == id:
#             return id
#         else:
#             return None


