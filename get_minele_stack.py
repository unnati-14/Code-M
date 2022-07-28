def __init__(self):
    self.s=[]
    self.minEle=None

def push(self,x):
    self.s.append(x)

def pop(self):
    if  len(self.s) is 0:
        return -1
    return self.s.pop()
    
def getMin(self):
    if (len(self.s) is 0):
        return -1
    return min(self.s)