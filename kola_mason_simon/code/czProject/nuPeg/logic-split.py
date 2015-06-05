import sys
import functools

def filesToDict(listOfFiles):
    '''
    >>> sorted(filesToDict(['test/image0Info.txt','test/image1Info.txt']).items())
    [('test/image0Info.txt', ['one', 'two']), ('test/image1Info.txt', ['three', 'four', 'three'])]

    '''
    return {f: open(f).read().splitlines() for f in listOfFiles}


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
