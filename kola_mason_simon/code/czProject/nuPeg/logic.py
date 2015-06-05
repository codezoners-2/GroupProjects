import sys
import functools


def filesToDict(files):
    """
    >>> filesToDict('test/testRead.txt')
    {'testImage3': 'data/images/numeric-countdown-wall.jpg', 'testImage2': 'data/images/blue-grass-tranz.jpg', 'testImage1': 'data/images/img-thing.jpg'}
    """
    return {file.split(',')[0]: file.split(',')[1] for file in open(files).read().splitlines()}


if __name__ == '__main__':
    import doctest
    doctest.testmod()
