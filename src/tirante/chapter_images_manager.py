from tirante.get_chapter_image_list import get_chapter_image_list


def chapter_images_list_to_csv(chapter_data):
    """
    Creates csv file for a chapter, given the list.
    chapter_data: A list containing a url and a title.
    """

    ch_name = ''.join([chapter_data[1], '.csv'])

    chapter_image_list = get_chapter_image_list(chapter_data)

    with open(ch_name, 'w') as outcsv:
        for image in chapter_image_list:
            outcsv.write(''.join([image[0], ',', image[1], '\n']))


def chapter_images_csv_to_list(chapter_image_csv):
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
