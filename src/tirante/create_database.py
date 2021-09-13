import os

# Project specific imports.
from tirante.get_chapters_list import get_chapters_list
from tirante.chapters_manager import chapters_list_to_csv
from tirante.chapters_manager import chapters_csv_to_list
from tirante.chapter_images_manager import chapter_images_list_to_csv


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
            chapter_images_list_to_csv(chapter)
        else:
            print(''.join([chapter_name_ext, ' already exists.']))
