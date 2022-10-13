from ImageCaptioner import Explainer
import matplotlib.pyplot as plt
from PIL import Image
import argparse


def main(image_name):
    EX = Explainer()
    image = Image.open(image_name).convert("RGB")
    data = EX.caption_generator(image_name)
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.title(data['caption'])
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--im', type=str)
    args = parser.parse_args()
    image_name = args.im
    main(image_name)

