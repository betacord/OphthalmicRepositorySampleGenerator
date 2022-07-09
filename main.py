import kaggle

from domain.repository import Repository
from domain.repository_type import RepositoryType
from utils.args import args
from utils.repository import get_random_sample


def main() -> None:
    kaggle.api.authenticate()

    repo = Repository(
        args.repository_url,
        args.data_output_filepath,
        args.full_data_tmp_path,
        args.repository_sample_output_path,
        list(RepositoryType)[args.repository_type],
        args.output_csv_filepath,
    )

    get_random_sample(repo)


if __name__ == '__main__':
    main()
