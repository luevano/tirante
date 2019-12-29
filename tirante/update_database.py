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

import os
from tirante.web_scrapping import get_chapter_list, get_chapter_image_list
from tirante.csv_manager import chapter_csv_to_list, image_list_to_csv


def update_database(manga_url,
                    manga_name,
                    database_dir):
    """
    Updates the database already created, adding missing elements.
    manga_url: url of the manga.
    manga_name: name of the manga.
    database_dir: directory where the database will be created.
    """

    # A better "naming" for the manga, for use with folder creation.
    # As well as the name of the main database.
    m_name = '_'.join(word.lower() for word in manga_name.split())
    m_name_ext = ''.join([m_name, '.csv'])

    # Navigate to database directory and create a new folder for the manga.
    init_folder = os.getcwd()
    os.chdir(database_dir)
    try:
        os.chdir(m_name)
    except FileNotFoundError:
        print(''.join([m_name,
                       ' folder doesn\'t exist.',
                       ' If you\'re trying to create the database for the',
                       ' first time, please use the create_database',
                       ' function instead.']))
        raise

    # First, download the data from the web.
    new_chapter_list = get_chapter_list(manga_url, manga_name, False)

    # And then, read the current database.
    last_chapter = chapter_csv_to_list(m_name_ext)[-1]

    # The missing chapters.
    missing_chapters = []
    for chapter in new_chapter_list:
        # If we get to the last acquired chapter, exit loop.
        if chapter == last_chapter:
            break
        missing_chapters.append(chapter)

    if not missing_chapters:
        print('Database already up to date.')
        return None

    # Reverse the order.
    missing_chapters = missing_chapters[::-1]

    # Write the last chapters to already existing csv file.
    # No need for checking if items are present,
    # since that's checked on the last steps,
    # that's how missing_chapters is acquired.
    with open(m_name_ext, 'a') as outcsv:
        for chapter in missing_chapters:
            outcsv.write(''.join([chapter[0], ',', chapter[1], '\n']))

    # Create the missing csv data files for each chapter.
    for chapter in missing_chapters:
        # Get the list for the images of each chapter.
        chapter_name_ext = ''.join([chapter[1], '.csv'])
        images_list = get_chapter_image_list(chapter)
        image_list_to_csv(images_list, chapter_name_ext)
    os.chdir(init_folder)
