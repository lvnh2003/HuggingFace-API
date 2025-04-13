import torch

from models import ImageRequest
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image


pipline = DiffusionPipeline.from_pretrained(
    "sd-legacy/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True,
)

pipline.enable_attention_slicing()

pipline.scheduler = DPMSolverMultistepScheduler.from_config(pipline.scheduler.config)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

pipline.to(device)
def generate_image(request: ImageRequest) -> Image:
    """
    Generate an image based on the provided request.

    Args:
        request (ImageRequest): The request object containing parameters for image generation.

    Returns:
        Image.Image: The generated image.
    """

    # Generate the image using the pipeline
    image: Image = pipline(
        prompt=request.prompt,
        negative_prompt=request.negative_prompt,
        width=request.width,
        height=request.height,
        num_inference_steps=request.num_inference_steps,
        guidance_scale=request.guidance_scale,
        strength=0.75,
    ).images[0]

    return image