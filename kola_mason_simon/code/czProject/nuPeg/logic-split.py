import sys
import functools


def filesToDict(listOfFiles):
    """
    >>> sorted(filesToDict(['static/test/image0Info.txt','static/test/image1Info.txt']).items())
    [('static/test/image0Info.txt', ['one', 'two']), ('static/test/image1Info.txt', ['three', 'four', 'three'])]

    """
    return {f: open(f).read().splitlines() for f in listOfFiles}


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
