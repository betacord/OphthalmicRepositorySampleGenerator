# Ophthalmic repository sample generator
Generator of pseudo random samples from publicly available repositories containing fundus photos.

## How to start
1. Download or clone the repository
2. Install Python interpreter: https://www.python.org/downloads/. When creating the tool, we used version 3.9.
3. Launch the terminal and navigate to the path containing the repository files
4. Install the required Python packages using the  following command
```
pip install -r requirements.txt
```

## How to run the tool
The tool's help can be obtained by running the following command in a terminal:
```
python main.py -h
```
then the screen will show the following output
```
usage: Random sample generator [-h] sample_size repository_url data_output_filepath full_data_tmp_path repository_sample_output_path repository_type output_csv_filepath

positional arguments:
  sample_size           An integer representing the size of the output random sample of photos from the repository.
  repository_url        A string representing a direct url of the image file. For the kaggle dataset, the schema is [username] / [dataset_id]. In the case of a kaggle competition, its ID.
  data_output_filepath  String representing the output file with the downloaded repository content.
  full_data_tmp_path    String representing the temporary path where the repository will be extracted to.
  repository_sample_output_path
                        A string representing the path where a randomly selected sample of the repository will be placed.
  repository_type       An integer representing the type of the repository source. 0 - classic url; 1 - kaggle competition; 2 - kaggle dataset.
  output_csv_filepath   String representing the path where the csv file will be saved (separated by ;) containing information about the repository.

optional arguments:
  -h, --help            show this help message and exit

```

Therefore, external parameters characterizing the size of the generated sample of images, data source, temporary paths, source type and paths to the output files should also be included in the invocation of the tool. An example of an invocation is shown below:
```
python main.py 10 retinopathy-classification-sai test.zip test test_sample 1 test.csv
```

If you have any questions or troubles you can ping me using e-mail that you can find at the website of Faculty of Mathematics and Computer Science, University of Warmia and Mazury, Poland.
