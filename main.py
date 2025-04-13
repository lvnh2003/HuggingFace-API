from models import ImageRequest
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import services
from io import BytesIO

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate-image")
async def generate_image(request: ImageRequest):
    """
    Generate an image based on the provided request.

    Args:
        request (ImageRequest): The request object containing parameters for image generation.

    Returns:
        StreamingResponse: The generated image as a streaming response.
    """
    image = services.generate_image(request)
    image_buffer = BytesIO()
    image.save(image_buffer, format="PNG")
    image_buffer.seek(0)
    return StreamingResponse(image_buffer, media_type="image/png")