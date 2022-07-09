from recordtype import recordtype

Repository = recordtype(
    'Repository',
    'url full_zip_path full_output_path sample_output_path repository_type repository_output_csv_path'
)
