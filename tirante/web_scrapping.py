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
from bs4 import BeautifulSoup
import re


# Thanks to https://stackoverflow.com/a/27086669 for this solution.
def del_multiple_chars(text, chars):
    """
    Deletes multiple characters in a text and returns the 'fixed' text.
    text: initial text.
    chars: string of chars to delete.
    """
    for c in chars:
        if c in text:
            text = text.replace(c, '')

    return text


def get_chapter_list(manga_url,
                     manga_name,
                     sort_list=True):
    """
    Retrieves chapter urls and names. Returns a list of lists
    containing the url and the title of the chapter.
    manga_url: url of the manga.
    manga_name: actual name of the manga, as it appears in the webpage.
    sort_list: sorting of the final array.
    """
    # Lowers the manga name string characters.
    manga_name = manga_name.lower()

    # Get the data from the html and parse it.
    page = requests.get(manga_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get the "rows" class, this contains the url
    # and title data for each chapter.
    soup_rows = soup.find_all('a', {'class': 'chapter-name'})

    # Creates a list to store data for each url and chapter name.
    chapter_list = []

    for row in soup_rows:

        # Gets the url name from the 'a' tag.
        href = row['href']
        # Same, for the title. Deletes every ocurrance of the manga name,
        # unwanted characters and then gets everyword.
        title = row['title'].lower()
        title = re.sub('vol.\d ', '', title)
        title = re.sub('vol.\d\d ', '', title)
        title = del_multiple_chars(title, '?:-_,\'').replace('...', '')
        title = title.replace(manga_name, '').replace('chapter', '')
        title = '_'.join(title.split())

        # Does sorcery to add zeros at the beginning of the name.
        if '_' in title:
            chapter_name = title.split('_')
            if '.' in chapter_name[0]:
                temp_name = chapter_name[0].split('.')
                temp_name[0] = temp_name[0].zfill(4)
                chapter_name[0] = '.'.join(temp_name)
            else:
                chapter_name[0] = chapter_name[0].zfill(4)
            chapter_name = '_'.join(chapter_name)
        else:
            chapter_name = title
            if '.' in chapter_name:
                temp_name = chapter_name.split('.')
                temp_name[0] = temp_name[0].zfill(4)
                chapter_name = '.'.join(temp_name)
            else:
                chapter_name = chapter_name.zfill(4)

        chapter_list.append([href, chapter_name])

    if sort_list:
        return chapter_list[::-1]
    else:
        return chapter_list


def get_chapter_image_list(chapter_data):
    """
    Gets the links for each image in the chapter,
        and returns a list of the image urls and its file name.
    chapter_data: a list containing a url and a title.
    NOTE: Not for direct use with the result of 'get_chapter_list'
    """
    # Get the data from the html and parse it.
    page = requests.get(chapter_data[0])
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get the "vung-doc" class, this contains a url for each page,
    # which redirects to the source of the image.
    # Deletes the first and last items, since they're trash.
    soup_img = soup.find_all('img')
    del soup_img[0]
    del soup_img[len(soup_img) - 1]

    # Stores each image url in a list.
    image_url_list = []
    for img in soup_img:
        # Gets the sring of the url, splits it by the char '/',
        # and gets the last item, which is the name of the file.
        original_img_name = img['src'].split('/')[-1]
        # Then, does sorcery to add zeros at the beginning of the name.
        img_name = original_img_name.split('.')
        img_name[0] = img_name[0].zfill(3)
        img_name = '.'.join(img_name)

        image_url_list.append([img['src'], img_name])

    return image_url_list
