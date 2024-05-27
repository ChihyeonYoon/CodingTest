class SmallestInfiniteSet(object):

    def __init__(self):
        self.q = [i for i in range(1,1001)]
        

    def popSmallest(self):
        """
        :rtype: int
        """
        return self.q.pop(0)
        

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num not in self.q:
            self.q.append(num)
            self.q.sort()
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)