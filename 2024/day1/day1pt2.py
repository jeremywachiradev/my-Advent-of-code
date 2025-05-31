left=[]
right=[]
#The """" thing is because it is a multiliner of an input and it would read well fr the .strip().split("\n")
input="""


"""


def solution(left,right):
    pairs=input.strip().split("\n")
    for pair in pairs:
        temp=pair.split()
        left.append(int(temp[0]))
        right.append(int(temp[1]))
        
           
    output=0
    for value in left:
        if value not in right:
            output+=0
        else:
            count=0
            for val in right:
                if val==value:
                    count+=1
            output+=(count*value)
        
    return output
    
print(solution(left,right))