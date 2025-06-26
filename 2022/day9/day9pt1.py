input="""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

"""
def solution(input):
    my_set=set()
    hr,hc,tr,tc=0,0,0,0
    head=(hr,hc)
    tail=(tr,tc)
    my_set.add((tr,tc))
    #keep track of the adding of the start position to the set
    for move in input:
        values=move.split(" ")
        for i in range(int(values[1])):
                hr,hc=head_movement(hr,hc,values)
                if abs(tr-hr)>1 or abs(tc-hc)>1:
                    tr,tc=tail_movement(hr,hc,tr,tc,values)


                if (tr,tc) not in my_set:
                    my_set.add((tr,tc))
    output=len(my_set)

    return output
def tail_movement(hr,hc,tr,tc,values):
    row_difference=hr-tr
    col_difference=hc-tc
    if abs(row_difference) > 1 or abs(col_difference) > 1:
        if row_difference != 0:
            if row_difference > 0:
                # if the head row is bigger than tail row ie head is somewhere beneath it in rows
                tr += 1
            else:
                tr -= 1
        if col_difference != 0:
            if col_difference > 0:
                # if the head column is bigger than the tail column ie the head is somehere to the right of the tail  
                tc += 1
            else:
                tc -= 1

    return tr,tc
def head_movement(hr,hc,values):
    match values[0]:
        case "U":
            hr-=1                    
        case "D":
              hr+=1
        case "L":
              hc-=1
        case "R":
              hc+=1
    return hr,hc
    




input=input.strip().split("\n")
print(solution(input))