import logging
import csv
from collections import defaultdict
from functools import reduce


def _transform_single_file(iostream):
    logging.info("Transforming file")
    reader = csv.DictReader(iostream)

    # Create a nested defaultdict so all users will automatically have zeros
    # for all paths
    result = defaultdict(lambda : defaultdict(int))
    for row in reader:
        user_id = int(row['user_id'])
        path = row['path']
        length = int(row['length'])
        result[user_id][path] += length
    return result


def _merge_transformed_data(dataset_1, dataset_2):
    for user_id, path_times in dataset_2.items():
        for path, time in path_times.items():
            dataset_1[user_id][path] += time
    return dataset_1


def _convert_to_standard_datastructs(dataset):
    '''
    Convert a defaultdict of defaultdicts to a list of dictionaries with
    consistent fields
    '''
    paths = set()
    for path_times in dataset.values():
        paths.update(path_times.keys())

    results = []
    for user_id, path_times in dataset.items():
        row = {'user_id': user_id}
        for path in paths:
            row[path] = path_times[path]
        results.append(row)

    return results


def transform(iostreams):
    converted_files = map(_transform_single_file, iostreams)
    reduced_data_set = reduce(_merge_transformed_data, converted_files)
    return _convert_to_standard_datastructs(reduced_data_set)
