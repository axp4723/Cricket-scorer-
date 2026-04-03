from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(
    title="Cricket Scorer API",
    description="Real-time cricket scoring application",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Cricket Scorer API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

# TODO: Add API routes
# - Teams management
# - Players management
# - Match management
# - Live scoring
# - Statistics
# - WebSocket endpoints

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)