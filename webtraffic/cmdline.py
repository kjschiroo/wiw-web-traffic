"""wttransform

Usage:
    wttransform [--verbose] --root_url=<web_log_url> <output_path>
    wttransform (-h | --help)

Options:
    -v, --verbose               Generate verbose output
    --baseurl=<web_log_url>     The base url for input csv dataset
    output_path                 The file to write results to
    -h, --help                  Print out this help text
"""
import logging
import csv
from docopt import docopt
from . import download
from . import transform


def _write_csv(dataset, output):
    try:
        fieldnames = list(dataset[0].keys())
    except IndexError:
        logging.error('Datasets were empty')
        return
    fieldnames.sort(reverse=True)
    dataset.sort(key=lambda row: row['user_id'])
    with open(output, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dataset)


def main():
    args = docopt(__doc__)
    if args['--verbose']:
        logging.basicConfig(level=logging.INFO)

    input_files = download.download_files_at(args['--root_url'])
    transformed_data = transform.transform(input_files)
    _write_csv(transformed_data, args['<output_path>'])


if __name__ == '__main__':
    main()
