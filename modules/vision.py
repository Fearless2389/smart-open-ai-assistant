# modules/vision.py

from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import torch

# Load the BLIP model and processor (slow on CPU, fast on GPU)
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

def analyze_image(image_file) -> str:
    """
    Uses BLIP to analyze an uploaded image and generate a question-based caption.
    Returns the interpreted text prompt for further use in the chat model.
    """
    try:
        image = Image.open(image_file).convert("RGB")

        # You can set a fixed question or make it dynamic later
        question = "What is happening in this image?"

        inputs = processor(image, question, return_tensors="pt")
        out = model.generate(**inputs)
        answer = processor.decode(out[0], skip_special_tokens=True)

        return f"Image Analysis: {answer}"

    except Exception as e:
        print(f"[Image Analysis Error] {e}")
        return "Sorry, I couldn't analyze the image."
