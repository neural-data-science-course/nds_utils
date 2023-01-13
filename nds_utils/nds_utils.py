import urllib.request
from os import remove
import zipfile


def download_data(url):
    '''
    Downloads the data folder from the given SURFdrive url into the current working directory.

    PARAMETRERS:
    url: string, Public url from NDS SURFdrive data repository
    '''

    if url.endswith('download'):
        URL = url
    else:
        URL = '/'.join((url, 'download'))

    if URL:
        response = urllib.request.urlopen(URL)
        data = response.read()
        response.close()

        with open('data.zip', 'wb') as f:
            f.write(data)

    with zipfile.ZipFile('data.zip', 'r') as zip_ref:
        zip_ref.extractall()

    remove('data.zip')
