class Solution:
    def binaryGap(self, N: int) -> int:
        indeces = list()
        binGaps = list()
        binGaps.append(0)
        binRep = bin(N)[2:]
        
        for x in range(0,len(binRep)):
            if binRep[x] == "1":
                indeces.append(x)
        
        for x in range(len(indeces)-1,0,-1):
            binGaps.append( indeces[x] - indeces[x-1] )
            #Order would be O(n) or O(2n)
                
        return max(binGaps)
    