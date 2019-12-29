"""MIT License

Copyright (c) 2019 David Luevano Alvarado

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import requests


def download_image(image,
                   save_img=True):
    """
    Downloads an image from the specified url,
        and saves it with the specified name.
    image: list that contains url and name.
    """

    # Gets the content of an image from its url.
    img_data = requests.get(image[0]).content

    if save_img:
        # Opens a file with its corresponding name as 'wb' (write, binary),
        # and then, writes the img_data.
        with open(image[1], 'wb') as handler:
            handler.write(img_data)
    else:
        return img_data


def download_chapter(image_list,
                     extra_status_msgs=False):
    """
    Downloads the whole chapter as images.
    image_list: list containing urls and file name for each image.
    extra_status_msgs: if each image status should be printed.
    """
    for image in image_list:
        if extra_status_msgs:
            print(image)
        download_image(image)
