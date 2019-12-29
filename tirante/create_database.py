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
from tirante.web_scrapping import get_chapters_list, get_chapter_image_list
from tirante.csv_manager import chapters_list_to_csv, images_list_to_csv


def create_database(manga_url,
                    manga_name,
                    database_dir):
    """
    Creates a database from zero, made of csv files.
    manga_url: url of the manga.
    manga_name: name of the manga.
    database_dir: directory where the database will be created.
    NOTE: This does not updates the database.
        If a database already exists, omits the creation of new files.
    """

    # A better "naming" for the manga, for use with folder creation.
    # As well as the name of the main database.
    m_name = '_'.join(word.lower() for word in manga_name.split())
    m_name_ext = ''.join([m_name, '.csv'])

    # Create the database folder and navigate to it.
    os.chdir(database_dir)
    try:
        os.mkdir(m_name)
        os.chdir(m_name)
    except FileExistsError:
        print(''.join([m_name,
                       ' folder already exists. If you\'re trying to update,',
                       ' please use the update_database function instead.']))
        os.chdir(m_name)

    # List of files and folders in the current path.
    data_list_dir = os.listdir()

    # Get the list of chapters, if this already exists,
    # read it from the database.
    # This is the main manga data.
    if m_name_ext not in data_list_dir:
        chapters_list = get_chapters_list(manga_url, manga_name)
        chapters_list_to_csv(chapters_list, m_name)
    else:
        print(''.join([m_name_ext,
                       ' already exists. If you\'re trying to update,',
                       ' please use the update_database function instead.']))
        return None

    # Data for each chapter.
    for chapter_data in chapters_list:
        # Get the list for the images of each chapter.
        chapter_name_ext = ''.join([chapter_data[1], '.csv'])
        if chapter_name_ext not in data_list_dir:
            images_list = get_chapter_image_list(chapter_data)
            images_list_to_csv(images_list, chapter_name_ext)
        else:
            print(''.join([chapter_name_ext,
                           ' already exists.',
                           ' If you\'re trying to update, please use',
                           ' the update_database function instead.']))
            return None
