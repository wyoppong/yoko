from fastapi import FastAPI, APIRouter

from routes import users

class Sprint(FastAPI):
    async def configure(self):
        self.include_router(users.router)


app = Sprint(
    title="Sprint", 
    description="Moving through"
    )

@app.on_event("startup")
async def startup():
    await app.configure()