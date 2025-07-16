input="""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().split("\n")
accumulator=0
LEN=len(input)
i=0
visited_set=set()
while i<LEN:
    instruction=input[i]
    
    visited_set.add(i)
    if instruction[:3]=="acc":
        temp=instruction.split(" ")
        accumulator+=int(temp[1])
        i+=1
    elif instruction[:3]=="jmp":
        temp=instruction.split(" ")
        i+=int(temp[1])
        if i in visited_set:
            break
    else:  
        i+=1
print(accumulator)

