from pydantic import BaseModel
from typing import Optional

class ImageRequest(BaseModel):
    prompt: str
    negative_prompt: Optional[str] = "low quality, lowres, wrong anatomy, bad anatomy, deformed, extra arms. missing arms, extra hands, extra fingers, missing fingers, red eyes, text, watermark, blurry, cropped, disfigured, ugly"
    width: Optional[int] = 512
    height: Optional[int] = 512
    num_inference_steps: Optional[int] = 25
    guidance_scale: Optional[float]= 7.5