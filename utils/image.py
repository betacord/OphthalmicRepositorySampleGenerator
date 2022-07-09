import os
from collections import Counter
from typing import Any

from matplotlib import image as mpimg

from consts.img_consts import IMG_EXTENSIONS


def get_img_extensions(file_list) -> list[Any]:
    extensions = map(lambda filename: os.path.splitext(filename)[-1][1:], file_list)
    extensions_counter = Counter(extensions)

    return list(filter(lambda ext: extensions_counter[ext] > 2 and ext.lower() in IMG_EXTENSIONS, extensions_counter))


def get_img_sizes(file_list) -> set[Any]:
    img_files = filter(lambda filename: os.path.splitext(filename)[-1][1:].lower() in IMG_EXTENSIONS, file_list)
    img_sizes = map(lambda filename: mpimg.imread(filename).shape, img_files)

    return set(img_sizes)
