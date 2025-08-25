import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket, WebSocketDisconnect

from app.routers import main_router
from app.services.websocket_manager import manager
app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:3000",
    "http://localhost:3001"
]
connected_clients: list[WebSocket] = []

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
app.include_router(main_router)
@app.get("/", include_in_schema=False)
def read_root():
  return {"message": "This is a backend service for Dashboard!"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
  await manager.connect(ws)
  try:
    while True:
      await ws.receive_text()
  except WebSocketDisconnect:
      manager.disconnect(ws)

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)