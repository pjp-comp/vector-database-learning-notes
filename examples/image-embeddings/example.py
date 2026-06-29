"""
IMAGE EMBEDDINGS — pictures become numbers too (and you can search them with words).

Reference: https://outcomeschool.com/blog/how-do-image-embeddings-work

Big idea:
    Just like text, an IMAGE can be turned into a list of numbers (an embedding)
    that captures what the image MEANS, not just its pixels. Two similar-looking
    images get similar numbers.

The magic model here is CLIP. CLIP puts images AND text into the SAME number-space.
That means you can search images using a text sentence — "cross-modal" search.

This demo:
    1. Draws a few simple colored shapes (no internet images needed).
    2. Embeds each image with CLIP.
    3. Image-to-image: finds which shapes are most similar to a red circle.
    4. Text-to-image: searches the images using the words "a red circle".

Run (from project root, venv active):
    python examples/image-embeddings/example.py
"""

import os

from PIL import Image, ImageDraw
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

HERE = os.path.dirname(__file__)


def make_shape(name, kind, color):
    """Draw a 128x128 image with one shape and save it. Returns (name, PIL image)."""
    img = Image.new("RGB", (128, 128), "white")
    draw = ImageDraw.Draw(img)
    box = [24, 24, 104, 104]
    if kind == "circle":
        draw.ellipse(box, fill=color)
    elif kind == "square":
        draw.rectangle(box, fill=color)
    elif kind == "triangle":
        draw.polygon([(64, 24), (24, 104), (104, 104)], fill=color)
    path = os.path.join(HERE, f"{name}.png")
    img.save(path)
    return name, img


# 1. Make a small gallery of shapes.
gallery = [
    make_shape("red_circle", "circle", "red"),
    make_shape("orange_circle", "circle", "orange"),
    make_shape("blue_square", "square", "blue"),
    make_shape("green_triangle", "triangle", "green"),
]
names = [n for n, _ in gallery]
images = [img for _, img in gallery]
print(f"Drew {len(images)} shape images: {', '.join(names)}\n")

# 2. Load CLIP — one model that understands BOTH images and text.
print("Loading the CLIP model (first run downloads it)...")
model = SentenceTransformer("clip-ViT-B-32")

# Embed all the images. Same idea as text: each image -> a list of numbers.
image_vectors = model.encode(images, normalize_embeddings=True)
print(f"Each image is now a list of {len(image_vectors[0])} numbers.\n")

# 3. IMAGE-TO-IMAGE: how similar is each image to the first one (red circle)?
print("Image-to-image: similarity to 'red_circle':")
sims = cos_sim(image_vectors[0], image_vectors)[0].tolist()
for name, score in sorted(zip(names, sims), key=lambda p: p[1], reverse=True):
    print(f"  {name:>15}  {score:0.3f}")

# 4. TEXT-TO-IMAGE (cross-modal): search the images using WORDS.
query = "a red circle"
print(f'\nText-to-image: searching the gallery for "{query}":')
text_vector = model.encode(query, normalize_embeddings=True)
sims = cos_sim(text_vector, image_vectors)[0].tolist()
for name, score in sorted(zip(names, sims), key=lambda p: p[1], reverse=True):
    print(f"  {name:>15}  {score:0.3f}")

print(
    "\nTakeaway:"
    "\n- Images become embeddings just like text does."
    "\n- CLIP shares ONE space for images and text, so words can find pictures."
    "\n- The PNGs were saved next to this script if you want to look at them."
)
