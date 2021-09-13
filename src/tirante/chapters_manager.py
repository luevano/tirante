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
