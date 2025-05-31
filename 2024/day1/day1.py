left=[]
right=[]
#The """" thing is because it is a multiliner of an input and it would read well fr the .strip().split("\n")
input="""
94370   90190
15509   72666
48816   23909
31300   40420
14729   97519

"""


def solution(left,right):
    pairs=input.strip().split("\n")
    for pair in pairs:
        temp=pair.split()
        left.append(int(temp[0]))
        right.append(int(temp[1]))
        
           
    output=0
    sleft=sorted(left)
    sright=sorted(right)
    for i,value in enumerate(sleft):
        output+=(max(value,sright[i])-min(value,sright[i]))
    return output
    
print(solution(left,right))