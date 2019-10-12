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
from create_database import create_database

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

if __name__ == "__main__":
    create_database(main_url=MAIN_URL,
                    manga_name_url=MANGA_NAME_URL,
                    manga_name=MANGA_NAME,
                    manga_dir=MANGA_DIR,
                    manga_data_dir=MANGA_DATA_DIR)
