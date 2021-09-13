import requests


def download_image(image_list):
    """
    Downloads an image from the specified url,
    and saves it with the specified name.
    image_list: list that contains url and name.
    """

    # Gets the content of an image from its url.
    img_data = requests.get(image_list[0]).content

    # Opens a file with its corresponding name as 'wb' (write, binary),
    # and then, writes the img_data.
    with open(image_list[1], 'wb') as handler:
        handler.write(img_data)


def download_chapter(image_list):
    """
    Downloads the whole chapter as images.
    image_url_list: List containing urls and file names for each image.
    """

    for image in image_list:
        print(image)
        download_image(image)
