"""This is a broken implementation, I couldn't make it work"""
def Sort_and_Count (A, start, end):
    if start==end:
        return 0
    else:
        mid = (start+end)//2
        x = Sort_and_Count(A, start, mid)
        y = Sort_and_Count(A, mid+1, end)
        z = CountSplitInv(A, start, end)
    return x+y+z

def CountSplitInv(A, start, end):
    if start==end:
        return 0;
    else:
        mid = (start+end)//2
        B = list()
        C = A[:mid+1]
        D = A[mid+1:end+1]

        count = 0
        """print(A[start:mid+1], A[mid+1:end+1]) for debugging"""

        while(len(C)!=0 or len(D)!=0):
            if len(C)!=0 and len(D)!=0 and C[0]<D[0]:
                B.append(C[0])
                C.pop(0)
            elif len(C)!=0 and len(D)!=0 and C[0]>D[0]:
                B.append(D[0])
                D.pop(0)
                count = count + len(C)
            elif len(C)!=0 and len(D)==0:
                B.append(C[0])
                C.pop(0)
            elif len(D)!=0 and len(C)==0:
                B.append(D[0])
                D.pop(0)

        print(B)
        i = start

        while (i<=end):
            A[i] = B[0]
            B.pop(0)
            i+=1
        return count

A = [7,6,5,4,3,2,1,0]

print(Sort_and_Count(A, 0, len(A)-1))