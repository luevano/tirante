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
from tirante.create_database import create_database
# from tirante.update_database import update_database
from tirante.download_manga import download_manga
from tirante.cbz_manager import zip_manga

# MANGA_URL = 'https://manganelo.com/manga/kimetsu_no_yaiba/'
MANGA_URL = 'https://manganelo.com/manga/read_boku_no_hero_academia_manga/'

# MANGA_NAME = 'Kimetsu no Yaiba'
MANGA_NAME = 'Boku No Hero Academia'

# PC main file location.
MANGA_DIR = 'E:\\Mangas\\'
# PC main manga data location.
DATABASE_DIR = 'test_data'

if __name__ == "__main__":
    create_database(MANGA_URL, MANGA_NAME, DATABASE_DIR)
    download_manga(MANGA_NAME, MANGA_DIR, DATABASE_DIR)
    zip_manga('E:\\Mangas\\Boku No Hero Academia')
