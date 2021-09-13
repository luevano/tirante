from tirante.create_database import create_database


def main() -> None:
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