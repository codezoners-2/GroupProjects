import sys
import functools


def filesToDict(files):
    """
    >>> filesToDict('static/test/testRead.txt')
    {'testImage3': 'static/assets/images/numeric-countdown-wall.jpg', 'testImage2': 'static/assets/images/blue-grass-tranz.jpg', 'testImage1': 'data/images/img-thing.jpg'}
    """
    return {file.split(',')[0]: file.split(',')[1] for file in open(files).read().splitlines()}


if __name__ == '__main__':
    import doctest
    doctest.testmod()
