import urllib3
from bs4 import BeautifulSoup


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
