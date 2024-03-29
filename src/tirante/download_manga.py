import os

# Project specific imports.
from tirante.chapters_manager import chapters_csv_to_list
from tirante.chapter_images_manager import chapter_images_csv_to_list
from tirante.download_manager import download_chapter


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
            chapter_image_list = chapter_images_csv_to_list(ch_name_ext)

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
