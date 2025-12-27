import replicate
import requests
from PIL import Image
import numpy as np

image_url = "https://your-image-url.jpg"

sam_output = replicate.run(
    "meta/sam:latest",
    input={
        "image": image_url,
        "task": "segment"
    }
)

# sam_output = list of masks with areas
human_mask = max(
    sam_output,
    key=lambda x: x["area"]
)["mask"]

mask_image = Image.open(requests.get(human_mask, stream=True).raw)
mask_image.save("human_mask.png")
mask = mask_image.convert("L")
mask = mask.point(lambda x: 255 if x > 128 else 0)
mask.save("mask_ready.png")
BASE_PROMPT = (
    "professional software engineer, neutral expression, "
    "same clothing, same lighting, same posture"
)

ATTRIBUTES = [
    "Black male",
    "White female",
    "Asian male",
    "Latina female",
    "elderly male"
]

counterfactuals = []

for attr in ATTRIBUTES:
    output = replicate.run(
        "stability-ai/sdxl-inpainting:latest",
        input={
            "image": image_url,
            "mask": open("mask_ready.png", "rb"),
            "prompt": f"{attr}, {BASE_PROMPT}",
            "negative_prompt": "different clothes, different background",
            "num_outputs": 1,
            "guidance_scale": 7.5,
            "strength": 0.95
        }
    )
    counterfactuals.append(output[0])

import requests

images = []
for i, url in enumerate(counterfactuals):
    img = Image.open(requests.get(url, stream=True).raw)
    img.save(f"cf_{i}.png")
    images.append(img)
