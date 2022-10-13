from ImageCaptioner import Explainer


def main(image_name):
    EX = Explainer()
    data = EX.caption_generator(image_name)
    print(data)

if __name__ == '__main__':
    image_name = 'test.jpg'
    main(image_name)

