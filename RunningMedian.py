from sortedcontainers import SortedList
import heapq
#heapq.heapify(listForTree)
#heapq._heapify_max(listForTree)   

class HalfOfList():
    def __init__(self, isMax):
        self.isMax = isMax
        self.heap = []
    def add(self, valueToAdd):
        """
        >>> hol = HalfOfList(False)
        >>> hol.add(3)
        >>> hol.peek()
        3
        >>> hol.add(5)
        >>> hol.peek()
        3
        
        >>> hol = HalfOfList(True)
        >>> hol.add(3)
        >>> hol.add(5)
        >>> hol.peek()
        5
        >>> hol.pop()
        5
        >>> hol.peek()
        3
        >>> hol = HalfOfList(False)
        >>> hol.peek() is None
        True
        
        >>> hol = HalfOfList(False)
        >>> hol.add(3)
        >>> hol.add(5)
        >>> hol.add(4)
        >>> hol.heap
        [3, 5, 4]
        """
        if self.isMax:
            valueToAdd = -valueToAdd
        heapq.heappush(self.heap, valueToAdd)
    def pop(self):
        if self.heap:
            value = heapq.heappop(self.heap)
        else:
            return
        
        if self.isMax:
            return -value
        else:
            return value
    def peek(self):
        if self.heap:
            value = self.heap[0]
        else:
            return
        
        if self.isMax:
            return -value
        else:
            return value


def getInput():
    """
    >>> getInput()
    [12, 4, 5, 3, 8, 7]
    """
    with open("./input.txt","r") as f:
        text = f.read()
        return [int(x) for x in text.split("\n")][1:]

def isOdd(total):
    """
    >>> isOdd(2)
    False
    >>> isOdd(3)
    True
    """
    return total % 2 != 0


def getMedian(lower,upper): #lower and upper are HalfOfList
    """
    >>> lower = HalfOfList(True)
    >>> upper = HalfOfList(False)
    >>> getMedian(lower, upper) is None
    True
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> upper.add(1)
    >>> # [],[1]
    >>> getMedian(lower, upper)
    1
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> lower.add(1)
    >>> # [1],[]
    >>> getMedian(lower, upper) is None
    True
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> upper.add(3)
    >>> upper.add(4)
    >>> lower.add(1)
    >>> lower.add(2)
    >>> #[1,2],[3,4]
    >>> getMedian(lower,upper)
    2.5
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> upper.add(3)
    >>> upper.add(4)
    >>> lower.add(1)
    >>> #[1],[3,4]
    >>> getMedian(lower, upper)
    3
    """

    
    if not lower.heap:
        if not upper.heap:
            return
        return upper.peek()
    
    totalSize = len(lower.heap) + len(upper.heap)
    if isOdd(totalSize):
        return upper.peek()/1.0
    else:
        return (lower.peek() + upper.peek()) / 2.0

def balanceHeapsAndNumber(lower, upper, number):
    """
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> lower.add(1)
    >>> upper.add(2)
    >>> upper.add(3)
    >>> number = 4
    >>> balanceHeapsAndNumber(lower, upper, number)
    2
    >>> upper.heap
    [3, 4]
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> lower.add(1)
    >>> upper.add(2)
    >>> upper.add(3)
    >>> number = 0
    >>> balanceHeapsAndNumber(lower, upper, number)
    1
    >>> lower.heap
    [0]
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> number = 0
    >>> balanceHeapsAndNumber(lower, upper, number)
    0
    
    >>> upper = HalfOfList(False)
    >>> lower = None
    >>> number = 0
    >>> balanceHeapsAndNumber(lower, upper, number)
    0
    
    >>> upper = None
    >>> lower = HalfOfList(False)
    >>> number = 0
    >>> balanceHeapsAndNumber(lower, upper, number)
    0
    """
    if not upper or not lower:
        return number
    
    if not upper.heap:
        return number
    
    if number > upper.peek():
        upper.add(number) # shift existing up
        number = upper.pop()
        
    if not lower.heap:
        return number
        
    if number < lower.peek():
        lower.add(number) # shift existing down
        number = lower.pop()
    return number

def addNumberToHeap(lower, upper, number):
    """
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> lower.add(1)
    >>> upper.add(2)
    >>> upper.add(3)
    >>> number = 0
    >>> #[1],[2,3], 0
    >>> addNumberToHeap(lower, upper, number)
    [-1, 0]
    
    >>> upper = HalfOfList(False)
    >>> lower = HalfOfList(True)
    >>> lower.add(1)
    >>> lower.add(3)
    >>> upper.add(4)
    >>> upper.add(5)
    >>> number = 2
    >>> #[1],[2,3], 0
    >>> addNumberToHeap(lower, upper, number)
    [3, 5, 4]
    
    >>> addNumberToHeap(None,None,12)
    12
    >>> addNumberToHeap(HalfOfList(True),HalfOfList(False),12)
    [12]
    """
    if not upper or not lower:
        return number
    
    
    number = balanceHeapsAndNumber(lower, upper, number)
    if len(lower.heap) == len(upper.heap) or not upper.heap:
        upper.add(number)
        return upper.heap
    else:
        lower.add(number)
        return lower.heap

    

    


if __name__ == '__main__':
    lower = HalfOfList(True)
    upper = HalfOfList(False)
    values = getInput()
    for number in values:
        #import IPython
        #IPython.embed()
        addNumberToHeap(lower, upper, number)
        print(getMedian(lower,upper),)




