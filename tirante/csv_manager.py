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


def chapters_list_to_csv(chapters_list,
                         manga_name):
    """
    Creates a csv file from a list of just scrapped data.
    chapters_list: list of data of the chapters.
    manga_name: name of the manga, file naming friendly.
    """

    # Adding '.csv' for csv creation.
    m_name_ext = ''.join([manga_name, '.csv'])

    with open(m_name_ext, 'w') as outcsv:
        for chapter in chapters_list:
            outcsv.write(''.join([chapter[0], ',', chapter[1], '\n']))


def chapters_csv_to_list(chapter_csv):
    """
    Gives a list of chaptesrs from a csv file.
    chapters_list: List of data of the chapters.
    """

    out_chapters_list = []

    with open(chapter_csv, 'r') as incsv:
        lines = incsv.readlines()
        for line in lines:
            out_chapters_list.append(line.strip().split(','))

    return out_chapters_list


def images_list_to_csv(images_list,
                       chapter_name_ext):
    """
    Creates csv file for a chapter from just scrapped data.
    images_list: list of data of images from a chapter.
    chapter_name_ext: name of the chapter with file extension included.
    """

    with open(chapter_name_ext, 'w') as outcsv:
        for image in images_list:
            outcsv.write(''.join([image[0], ',', image[1], '\n']))


def images_csv_to_list(chapter_image_csv):
    """
    Returns a list of chapter images from a csv file.
    chapter_image_csv: csv containing data for the chapter.
    """

    out_chapter_image_list = []

    with open(chapter_image_csv, 'r') as incsv:
        lines = incsv.readlines()
        for line in lines:
            out_chapter_image_list.append(line.strip().split(','))

    return out_chapter_image_list
