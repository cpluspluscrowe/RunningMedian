from sortedcontainers import SortedList

def getInput():
    """
    >>> getInput()
    [12, 4, 5, 3, 8, 7]
    """
    with open("./input.txt","r") as f:
        text = f.read()
        return [int(x) for x in text.split("\n")][1:]

def getMedian(l):
    """
    >>> getMedian([1,2,3])
    2.0
    >>> getMedian([1,2])
    1.5
    >>> getMedian([1,2,3,4])
    2.5
    >>> getMedian([]) is None
    True
    >>> getMedian([1])
    1.0
    """
    if not l:
        return
    
    def getMiddleIndex(l):
        """
        >>> getMiddleIndex([1,2,3])
        1
        >>> getMiddleIndex([1,2])
        1
        >>> getMiddleIndex([1,2,3,4])
        2
        """
        return int(len(l)/2)
    
    def isOddCount(l):
        """
        >>> isOddCount([1,2])
        False
        >>> isOddCount([1,2,3])
        True
        """
        return len(l) % 2 != 0
    
    mi = getMiddleIndex(l)
    if isOddCount(l) or mi == 0:
        return l[mi]/1.0
    else:
        return (l[mi] + l[mi-1])/2
    
if __name__ == '__main__':
    runningList = SortedList()
    values = getInput()
    for number in values:
        runningList.add(number)
        print(getMedian(runningList))




