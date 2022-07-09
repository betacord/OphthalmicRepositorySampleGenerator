from argparse import ArgumentParser

from consts import arg_strings


def create_parser() -> ArgumentParser:
    arg_parser = ArgumentParser('Random sample generator')
    arg_parser.add_argument('sample_size', help=arg_strings.SAMPLE_SIZE_HELP, type=int)
    arg_parser.add_argument('repository_url', help=arg_strings.REPOSITORY_URL_HELP, type=str)
    arg_parser.add_argument('data_output_filepath', help=arg_strings.OUTPUT_FILE_PATH_HELP, type=str)
    arg_parser.add_argument('full_data_tmp_path', help=arg_strings.TEMP_FULL_DATA_PATH_HELP, type=str)
    arg_parser.add_argument('repository_sample_output_path', help=arg_strings.REPOSITORY_SAMPLE_OUTPUT_PATH, type=str)
    arg_parser.add_argument('repository_type', help=arg_strings.REPOSITORY_TYPE_HELP, type=int)
    arg_parser.add_argument('output_csv_filepath', help=arg_strings.REPOSITORY_INFO_OUTPUT_PATH, type=str)

    return arg_parser


args = create_parser().parse_args()
