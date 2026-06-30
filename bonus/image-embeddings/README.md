# Image embeddings — pictures become numbers too

**Big idea:** the same trick that turns *text* into meaning-numbers also works on
*images*. Two similar-looking images get similar numbers. And with **CLIP**, images
and text live in the **same** number-space — so you can search pictures using words.

Reference: [How do image embeddings work? (Outcome School)](https://outcomeschool.com/blog/how-do-image-embeddings-work)

## Run
```bash
python bonus/image-embeddings/example.py
```
(First run downloads the CLIP model. The demo draws its own shapes, so no internet
images are needed. The PNGs are saved next to the script.)

## What you'll see
1. **Image-to-image** — a red circle is most similar to an orange circle, less so
   to a square or triangle.
2. **Text-to-image (cross-modal)** — the words *"a red circle"* find the red-circle
   image. Text searching images — that's CLIP's superpower.

## Words to know
- **Image embedding** — a list of numbers capturing what an image *means*, not its raw pixels.
- **CNN / Vision Transformer** — neural nets that build the embedding (edges → parts → objects).
- **CLIP** — a model that embeds images *and* text into one shared space.
- **Cross-modal search** — searching one type (images) with another (text).

→ Full explanation: [learning_notes.md](../../learning_notes.md#deep-dive-image-embeddings-searching-pictures)
