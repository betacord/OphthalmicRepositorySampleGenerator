import os
import zipfile
from glob import glob
from random import sample
from shutil import copy, make_archive, rmtree
from typing import Callable, Any, Tuple, List, Union, Set

import kaggle
import requests
from hurry.filesize import size
from pyunpack import Archive

from consts.img_consts import IMG_EXTENSIONS
from domain.repository_type import RepositoryType
from utils.args import args
from utils.image import get_img_extensions, get_img_sizes


def get_repository_download_command(repository) -> Callable[[Any], Any]:
    if repository.repository_type == RepositoryType.url:
        return lambda: requests.get(repository.url, verify=False)
    elif repository.repository_type == RepositoryType.kaggle_competition:
        return lambda: kaggle.api.competition_download_files(repository.url)
    elif repository.repository_type == RepositoryType.kaggle_dataset:
        return lambda: kaggle.api.dataset_download_files(repository.url)


def unpack_repository(repository) -> None:
    file_extension = repository.full_zip_path.split('.')[-1]

    if file_extension == 'zip':
        with zipfile.ZipFile(repository.full_zip_path, 'r') as zip_ref:
            zip_ref.extractall(repository.full_output_path)
    elif file_extension in ('rar', '7z'):
        os.mkdir(repository.full_output_path)
        Archive(repository.full_zip_path).extractall(repository.full_output_path)


def get_and_unpack_repository(repository) -> int:
    download_repo_command = get_repository_download_command(repository)
    download_response = download_repo_command()

    if isinstance(download_response, requests.models.Response):
        with open(repository.full_zip_path, 'wb') as output_file:
            output_file.write(download_response.content)

    if repository.repository_type in (RepositoryType.kaggle_competition, RepositoryType.kaggle_dataset):
        if repository.repository_type == RepositoryType.kaggle_dataset:
            repository.url = repository.url[repository.url.find('/') + 1:]

        repository.full_zip_path = f'{os.getcwd()}/{repository.url}.zip'

    unpack_repository(repository)

    return size(os.path.getsize(repository.full_zip_path))


def get_random_sample(repository) -> tuple[int, Any, int, Any]:
    local_sample_size = args.sample_size

    repo_size = get_and_unpack_repository(repository)

    list_imgs = [f for f in glob(f'{repository.full_output_path}/**/*.*', recursive=True)
                 if os.path.splitext(f)[-1][1:].lower() in IMG_EXTENSIONS]

    repo_img_extensions = get_img_extensions(list_imgs)
    repo_img_count = len(
        list(filter(lambda filename: os.path.splitext(filename)[-1][1:].lower() in IMG_EXTENSIONS, list_imgs))
    )
    repo_img_sizes = get_img_sizes(list_imgs)

    if local_sample_size > len(list_imgs):
        local_sample_size = len(list_imgs)

    random_img_paths = sample(list_imgs, local_sample_size)

    os.mkdir(repository.sample_output_path)

    for img_path in random_img_paths:
        copy(img_path, repository.sample_output_path)

    make_archive(repository.sample_output_path, 'zip', repository.sample_output_path)

    rmtree(repository.full_output_path, ignore_errors=True)
    rmtree(repository.sample_output_path, ignore_errors=True)
    os.remove(repository.full_zip_path)

    output_info = str(repo_size), str(repo_img_extensions), str(repo_img_count), str(repo_img_sizes)

    open(repository.repository_output_csv_path, 'a').write(';'.join(output_info))

    return repo_size, repo_img_extensions, repo_img_count, repo_img_sizes
