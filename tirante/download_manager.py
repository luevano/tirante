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
