"""
Given a train track with some trains on it, then the same train track
after some time has passed, return True if the arrangement is valid, otherwise return False
"""

def is_valid_train_arrangement(before, after):
    l=len(before)
    if not l==len(after):
        return False
    blist=[[i,before[i]] for i in range(l) if before[i] in ["<",">"]]
    alist=[[i,after[i]] for i in range(l) if after[i] in ["<",">"]]
    l=len(blist)
    if l!=len(alist):
        return False
    for i in range(l):
        if not blist[i][1]==alist[i][1]:
            return False
        if blist[i][1]==">" and blist[i][0]>alist[i][0]:
            print(blist[i][1],blist[i][0],alist[i][0])
            return False
        if blist[i][1]=="<" and blist[i][0]<alist[i][0]:
            return False      
    return True