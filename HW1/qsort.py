import sys

def qsort(arry):
    if arry == []:
        return []
    else:
        pivot = arry[0]
        left = [x for x in arry if x < pivot]
        right = [y for y in arry[1:] if y >= pivot]
        return [qsort(left)] + [pivot] + [qsort(right)]

def sorted(tree):
    if tree == []:
        return []
    left,pivot,right = tree
    return sorted(left) + [pivot] +sorted(right)


def _search(tree,num):
    if tree == []:
        return tree

    left,root,right = tree
    if root == num:
        return tree
    elif num < root:
        return _search(left,num)
    else:
        return _search(right,num)

##def _search(tree, x):
##    if tree == [] or tree[1] == x:
##        return tree
##    return _search(tree[0], x) if x < tree[1] else _search(tree[2], x)


def search(tree,num):
    if _search(tree,num) == []:
       return False
    else:
        return True


def insert(tree,num):
    x = _search(tree,num)
    if x == []:
       x+=[[],num,[]]



if __name__ == "__main__":
    print "original array"
    x = [3,5,2,7,8,1,6]
    print x
    
    tree = qsort(x)
    print "The buggy tree structure"
    print tree

    d =sorted(tree)
    print "The new array sorted by tree"
    print d

    print " _search subtree contains 5"
    print _search(tree,5)

    print "search 6, should be True"
    print search(tree,6)
    print "search 11, should be False"
    print search(tree,11)

    print"Array that insert 6.5"
    insert(tree,6.5)
    print tree
    print "Array that insert 7, should be the original one"
    insert(tree,7)
    print tree
