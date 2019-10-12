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
import urllib3
from bs4 import BeautifulSoup


def get_chapters_list(main_url,
                      manga_name_url,
                      manga_name,
                      reverse_sorted=True):
    """
    Retrieves chapter urls and names. Returns a list of lists
    containing the url and the title of the chapter.
    main_url: Main webpage name (source).
    manga_name_url: Name of the manga in the url format
    that's used by the webpage.
    manga_name: Actual name of the manga, as it appears in the webpage.
    reverse_sorted: Sorting of the final array.
    """

    manga_url = ''.join([main_url, manga_name_url])

    # Not actually a file, but the content of the html.
    html = urllib3.PoolManager().request('GET', manga_url)

    # Get the data from the html and parse it.
    soup = BeautifulSoup(html.data, 'html.parser')

    # Get the "rows" class, this contains the url
    # and title data for each chapter.
    # Deletes the first tag, since it's not useful.
    soup_rows = soup.find_all('div', {'class': 'row'})
    del soup_rows[0]

    # Creates a list to store date for each url and chapter name.
    chapter_list = []

    for row in soup_rows:

        # Gets the url name from the a tag.
        href = row.a['href']
        # Same, for the title. Deletes every ocurrance of the manga name,
        # unwanted characters and then gets everyword.
        title_words = row.a['title'].replace(manga_name, '').replace('?', '')
        title_words = title_words.replace(':', '').replace('-', '')
        title_words = title_words.replace('...', '').replace(',', '').split()

        # Doing all the work in oneliner doesn't work for some chapters,
        # for some reason.
        # title = '_'.join(row.a['title'].replace(manga_name, '')
        # .replace(':', '').replace('-', '').lower().split())

        # Lowers every word and appends it to a new list,
        # then it gets joined with '_' as a sep.
        title_words_lower = []
        for word in title_words:
            title_words_lower.append(word.lower())

        title = '_'.join(title_words_lower)

        # print(href, title)
        chapter_list.append([href, title])

    if reverse_sorted:
        return chapter_list[::-1]
    else:
        return chapter_list
