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
import os
import urllib3
from bs4 import BeautifulSoup
import requests

# Project specific imports.
from gcl import get_chapters_list


def chapters_list_to_csv(chapters_list,
                         manga_name):
    """
    Creates a csv file from the input chapter_list.
    chapters_list: List of data of the chapters.
    manga_name: Name of the manga, folder naming friendly.
    """

    # Adding '.csv' for csv creation.
    m_name_ext = ''.join([manga_name, '.csv'])
    # print(m_name)

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


def get_chapter_image_list(chapter_data):
    """
    Gets the links for each image in the chapter,
    and returns a list of the links.
    Returns a list of the image urls and its file name.
    chapter_data: A list containing a url and a title.
    NOTE: Not for direct use with the result of 'get_chapters_list'
    """

    # Not actually a file, but the content of the html.
    html = urllib3.PoolManager().request('GET', chapter_data[0])

    # Get the data from the html and parse it.
    soup = BeautifulSoup(html.data, 'html.parser')

    # Get the "vung-doc" class, this contains a url for each page,
    # which redirects to the source of the image.
    # Deletes the first and last items, since they're trash.
    soup_img = soup.find_all('img')
    del soup_img[0]
    del soup_img[len(soup_img)-1]

    # Stores each image url in a list.
    image_url_list = []
    for img in soup_img:
        # Gets the sring of the url, splits it by the char '/',
        # and gets the last item, which is the name of the file.

        image_url_list.append([img['src'], img['src'].split('/')[-1]])

    return image_url_list


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


def create_database(main_url,
                    manga_name_url,
                    manga_name,
                    manga_dir,
                    manga_data_dir):
    """
    Creates a database from zero, made of csv files.
    main_url: Main webpage name (source).
    manga_name_url: Name of the manga in the url format
    that's used by the webpage.
    manga_name: Actual name of the manga, as it appears in the webpage.
    manga_dir: Main manga folder in computer, subfolders here will be created.
    manga_data_dir: Main manga data folder in computer.
    NOTE: This does not updates the database.
    If a database already exists, omits the creation of new files.
    """

    # A better "naming" for the manga, for use with folder creation.
    # As well as the name of the main database.
    m_name = '_'.join(word.lower() for word in manga_name.split())
    m_name_ext = ''.join([m_name, '.csv'])

    # Navigate to where the main data folder is,
    # then to where the manga folder is.
    os.chdir(manga_data_dir)
    try:
        os.mkdir(m_name)
        os.chdir(m_name)
    except FileExistsError:
        print(''.join([m_name,
                       ' folder already exists.']))
        os.chdir(m_name)

    # List of files and folders in the current path.
    data_list_dir = os.listdir()

    # Get the list of chapters, if this already exists,
    # read it from the database.
    # This is the main manga data.
    if m_name_ext not in data_list_dir:
        chapters_list = get_chapters_list(main_url=main_url,
                                          manga_name_url=manga_name_url,
                                          manga_name=manga_name)
        chapters_list_to_csv(chapters_list=chapters_list, manga_name=m_name)
    else:
        print(''.join([m_name_ext, ' already exists.']))
        chapters_list = chapters_csv_to_list(m_name_ext)

    # Data for each chapter.
    for chapter in chapters_list:
        # Get the list for the images of each chapter.
        chapter_name_ext = ''.join([chapter[1], '.csv'])
        if chapter_name_ext not in data_list_dir:
            chapter_image_list_to_csv(chapter)
        else:
            print(''.join([chapter_name_ext, ' already exists.']))


def update_database(main_url,
                    manga_name_url,
                    manga_name,
                    manga_dir,
                    manga_data_dir):
    """
    Updates the database already created, adding missing ones.
    main_url: Main webpage name (source).
    manga_name_url: Name of the manga in the url format
    that's used by the webpage.
    manga_name: Actual name of the manga, as it appears in the webpage.
    manga_dir: Main manga folder in computer, subfolders here will be created.
    manga_data_dir: Main manga data folder in computer.
    """

    # A better "naming" for the manga, for use with folder creation.
    # As well as the name of the main database.
    m_name = '_'.join(word.lower() for word in manga_name.split())
    m_name_ext = ''.join([m_name, '.csv'])

    # Navigate to where the main data folder is,
    # then to where the manga folder is.
    os.chdir(manga_data_dir)
    try:
        os.mkdir(m_name)
        os.chdir(m_name)
    except FileExistsError:
        print(''.join([m_name,
                       ' folder already exists.']))
        os.chdir(m_name)

    # Get a list of files present in path.
    data_list_dir = os.listdir()

    # First, download the data from the web.
    new_chapter_list = get_chapters_list(main_url=main_url,
                                         manga_name_url=manga_name_url,
                                         manga_name=manga_name,
                                         reverse_sorted=False)

    # And then, read the current database.
    last_chapter = chapters_csv_to_list(m_name_ext)[-1]

    # The missing chapters.
    missing_chapters = []
    for chapter in new_chapter_list:
        # If we get to the last acquired chapter, exit loop.
        if chapter == last_chapter:
            break
        missing_chapters.append(chapter)

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
        if chapter_name_ext not in data_list_dir:
            chapter_image_list_to_csv(chapter)
        else:
            print(''.join([chapter_name_ext, ' already exists.']))


def download_image(image_list):
    """
    Downloads an image from the specified url,
    and saves it with the specified name.
    image_list: list that contains url and name.
    """

    # Gets the content of an image rom its url.
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


def download_manga(manga_name,
                   manga_dir,
                   manga_data_dir):
    """
    Downloads a whole manga, saving it to subfolders.
    Uses the database already created.
    that's used by the webpage.
    manga_name: Actual name of the manga, as it appears in the webpage.
    manga_dir: Main manga folder in computer, subfolders here will be created.
    manga_data_dir: Main manga data folder in computer.
    NOTE: This updates the manga, downloading the missing chapters
    if they're listed in the database.
    """

    # A better "naming" for the manga, for use with folder creation.
    # As well as the name of the main database.
    m_name = '_'.join(word.lower() for word in manga_name.split())
    m_name_ext = ''.join([m_name, '.csv'])

    # Go to where the database is located.
    os.chdir(manga_data_dir)
    try:
        os.chdir(m_name)
    except FileNotFoundError:
        print(''.join([m_name,
                       ' folder doesn\'t exist.',
                       ' Most likely, the database hasn\'t been created.']))
        raise NameError('Create database first.')

    # Get info of the files in the database.
    data_list_dir = os.listdir()

    # Reads data from the main database.
    if m_name_ext not in data_list_dir:
        print(''.join([m_name,
                       ' database hasn\'t been created.',
                       ' Most likely, the database hasn\'t been created.']))
        raise NameError('Create database first.')
    else:
        chapters_list = chapters_csv_to_list(m_name_ext)

    # Navigate to the main manga dir,
    # and either create or go to manga folder.
    os.chdir(manga_dir)
    try:
        os.mkdir(manga_name)
        os.chdir(manga_name)
    except FileExistsError:
        print(''.join([manga_name,
                       ' folder already exists.']))
        os.chdir(manga_name)

    # Get data of the folders in the manga folder.
    manga_list_dir = os.listdir()

    for chapter in chapters_list:
        # chapter_url = chapter[0]
        chapter_name = chapter[1]
        ch_name_ext = ''.join([chapter_name, '.csv'])

        if chapter_name not in manga_list_dir:
            print(''.join(['Downloading ',
                           chapter_name,
                           ' now.']))
            # First, create the chapter folder.
            os.mkdir(chapter_name)

            # Go to where the database is located.
            os.chdir(manga_data_dir)
            os.chdir(m_name)
            chapter_image_list = chapter_image_csv_to_list(ch_name_ext)

            # Go back to where the manga is going ot be downloaded.
            os.chdir(manga_dir)
            os.chdir(manga_name)
            os.chdir(chapter_name)

            # Download all the chapter images on its respective folder.
            download_chapter(chapter_image_list)

            # Go back one folder to repeat the process
            # for the next chapter.
            os.chdir('..')
        else:
            print(''.join([chapter_name,
                           ' already downloaded.']))
