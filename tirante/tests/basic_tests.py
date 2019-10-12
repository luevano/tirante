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
from tirante import create_database

# Main manga source.
MAIN_URL = 'https://manganelo.com/manga/'
# Manga name.
MANGA_NAME = 'Kimetsu no Yaiba'
# Manga name in the form of how appears in the url.
MANGA_NAME_URL = 'kimetsu_no_yaiba/'

# PC main file location.
MANGA_DIR = 'E:\\Mangas\\'
# PC main manga data location.
MANGA_DATA_DIR = ''.join(['C:\\Users\\Lorentzeus\\Google Drive\\',
                          'Personal\\Python\\tirante\\test_data'])

create_database(main_url=MAIN_URL,
                manga_name_url=MANGA_NAME_URL,
                manga_name=MANGA_NAME)
# update_database()
# download_manga()

# print(os.listdir())

# chapter_csv_to_df(chapter_csv='kimetsu_no_yaiba.csv')
# download_manga()

# chapter_list = get_chapters_list()
# for chapter in chapter_list:
#     print(chapter)

# chapters_list_to_csv(chapters_list=chapter_list)

# os.chdir('data/kimetsu_no_yaiba')
# for image in chapter_image_csv_to_list('chapter_1_cruelty.csv'):
#    print(image)

# chapters_list = chapters_csv_to_list(chapter_csv='kimetsu_no_yaiba.csv')

# chapter_image_list_to_csv(chapters_list[0])


# first_chapter_img_url_list = get_chapter_image_list(chapter_list[0])

# download_image(first_chapter_img_url_list[0])


# os.chdir(MANGA_DIR)

# download_chapter(first_chapter_img_url_list)
