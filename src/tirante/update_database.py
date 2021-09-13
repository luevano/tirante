import os

# Project specific imports.
from tirante.get_chapters_list import get_chapters_list
from tirante.chapters_manager import chapters_csv_to_list
from tirante.chapter_images_manager import chapter_images_list_to_csv


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
            chapter_images_list_to_csv(chapter)
        else:
            print(''.join([chapter_name_ext, ' already exists.']))
