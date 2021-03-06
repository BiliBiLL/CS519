import math

def find(tree,x,best = None):
    if tree == [] or tree == None:
        return best
    left,root,right = tree
    if best == None or abs(root - x) < abs(best - x):
        best = root
    if x<root:
        return find(left,x,best)
    else:
        return find(right,x,best)


if __name__ == "__main__":
    t = [[[],2,[]],4,[[[],5,[]],6,[[],7,[]]]]
    print find(t,4.7)
