"""MIT License

Copyright (c) 2019 David Luevano

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
from .gcil import get_chapter_image_list


def chapter_image_list_to_csv(chapter_data):
    """
    Creates csv file for a chapter, given the list.
    chapter_data: A list containing a url and a title.
    """

    ch_name = ''.join([chapter_data[1], '.csv'])

    chapter_image_list = get_chapter_image_list(chapter_data)

    with open(ch_name, 'w') as outcsv:
        for image in chapter_image_list:
            outcsv.write(''.join([image[0], ',', image[1], '\n']))


def chapter_image_csv_to_list(chapter_image_csv):
    """
    Returns a list given the csv file.
    chapter_image_csv: csv containing data for the chapter.
    """

    out_chapter_image_list = []

    with open(chapter_image_csv, 'r') as incsv:
        lines = incsv.readlines()
        for line in lines:
            # print(line.strip().split(','))
            out_chapter_image_list.append(line.strip().split(','))

    return out_chapter_image_list
