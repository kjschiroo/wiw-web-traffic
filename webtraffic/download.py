import logging
import io
import requests
import string
from . import errors


def _get_file_urls(root_url):
    url_template = '{url}{file_name}.csv'
    return [
        url_template.format(url=root_url, file_name=letter)
        for letter in string.ascii_lowercase
    ]


def _try_request_file(file_url, session, retries):
    for i in range(retries):
        try:
            response = session.get(file_url, timeout=5)
            break
        except requests.exceptions.ConnectionError:
            logging.info(
                'Download failed, retrying download for {0}'.format(file_url)
            )
    else:
        raise errors.Error('File {0} could not be downloaded'.format(file_url))
    return response


def download_files_at(root_url, retries=5):
    '''
    Download all expected files at the root_url and return an iterator of io
    streams
    '''
    session = requests.Session()
    for file_url in _get_file_urls(root_url):
        logging.info('Downloading {0}'.format(file_url))
        response = _try_request_file(file_url, session, retries)
        logging.info('Download complete')

        # Convert the response content to StringIO so we can treat it as a file
        # handle without needing to save it.
        yield io.StringIO(response.content.decode())
