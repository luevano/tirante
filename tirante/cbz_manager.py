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
import os
import zipfile as zf


# IMPORTANT NOTE: A CBX FILE NEEDS TO HAVE ITS CONTENTS !!!SORTED!!! FOR
# THEM TO BE DISPLAYED. I noticed this thanks to a fantastic code i found in
# https://github.com/Lightjohn/CbXManager/blob/master/cbxmanager.py
# that gave me the insight I needed to finish the zipping of the files. Before,
# I only had corrupt files because I was missing the sorting part.

# And thanks to https://stackoverflow.com/a/6743512 for this pieces of code.
# Although I don't need it anymore since I solved the problem from the source.
def sort_numerically(list, key='ch_img'):
    """
    Sorts files numerically instead of alphabetically.
    NOTE: only works for files named '1.x', '10.y', etc.
    """
    accepted = {'ch_img': '.', 'ch_name': '_'}
    if key in accepted.keys():
        return sorted(list, key=lambda x: float(x.split(accepted[key])[0]))
    else:
        print(''.join(['Error. Key \'',
                       key,
                       '\' is not valid.']))
        raise NameError('Invalid key-name.')


def zip_chapter(chapter_name):
    """
    Zips a chapter into the desired extension.
    chapter_name: name of the chapter. This is also the folder name.
    """
    # Naming for the zip file, just a combination of
    # the chapter name and the extension.
    zf_name = '.'.join([chapter_name, 'cbz'])
    with zf.ZipFile(zf_name, 'w', zf.ZIP_DEFLATED, False, 9) as zip_file:
        # Change to the chapter folder and
        # get a list of all image files.
        os.chdir(chapter_name)
        image_list = os.listdir()
        os.chdir('..')
        for image in image_list:
            zip_file.write('\\'.join([chapter_name, image]))


def zip_manga(manga_dir):
    """
    Zips a whole manga.
    manga_dir: directory where the manga is stored.
    save_dir: where to save the compressed manga.
    """
    os.chdir(manga_dir)
    chapter_list = os.listdir()

    for chapter in chapter_list:
        if '.'.join([chapter, 'cbz']) not in chapter_list:
            if chapter.split('.')[-1] != 'cbz':
                zip_chapter(chapter)
