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


def get_chapters_list(manga_url,
                      manga_name,
                      sort_list=True):
    """
    Retrieves chapter urls and names. Returns a list of lists
    containing the url and the title of the chapter.
    manga_url: url of the manga.
    manga_name: actual name of the manga, as it appears in the webpage.
    sort_list: sorting of the final array.
    """
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
        title = re.sub('Vol.\d ', '', row['title'])
        title = re.sub('Vol.\d\d ', '', row['title'])
        title = '_'.join(title.replace(manga_name, '').replace('?', '')
                         .replace(':', '').replace('-', '').replace('...', '')
                         .replace(',', '').lower().split())

        print(href, title)
        chapter_list.append([href, title])

    if sort_list:
        return chapter_list[::-1]
    else:
        return chapter_list


get_chapters_list('https://manganelo.com/manga/kimetsu_no_yaiba/',
                  'Kimetsu no Yaiba')
