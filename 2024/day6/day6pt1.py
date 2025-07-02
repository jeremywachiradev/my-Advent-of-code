input ="""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

""".strip().split("\n")
height=len(input)
width=len(input[0])
obstacle="#"
empty="."
initial_position=[]
for str_index,thing in enumerate(input):
    for char_index,char in enumerate(thing):
        if char !=empty and char !=obstacle:
            initial_position.append(str_index)
            initial_position.append(char_index)

def turn(guard):
    if guard=="^":
        return ">"
    elif guard==">":
        return "v"
    elif guard=="v":
        return "<"
    elif guard=="<":
        return "^"
def actually_turn(stringy,index,symbol):
    # print(stringy)
    new_str=""
    for char_index,char in enumerate(stringy):
        if char_index==index:
            new_str=new_str+symbol
        else:
            new_str=new_str+char
    return new_str
def replace(input,coordinate):
    new_str=""
    for char_index,char in enumerate(input[coordinate[0]]):
        if char_index==coordinate[1]:
            new_str=new_str+"X"
        else:
            new_str=new_str+char
    return new_str
def place_direction(input,coordinate,symbol):
    new_str=""
    for char_index,char in enumerate(input[coordinate[0]]):
        if char_index==coordinate[1]:
            new_str=new_str+symbol
        else:
            new_str=new_str+char
    return new_str
def traverse(direction,input):
    while True:
        guard=input[direction[0]][direction[1]]
        if guard=="^":
            
            if direction[0]-1<0:
                break
                return
            next_position=input[direction[0]-1][direction[1]]
            if next_position==obstacle:
                # print("this happens")
                new_direction=turn(guard)
                input[direction[0]]=actually_turn(input[direction[0]],direction[1],new_direction)
                
            else:
                input[direction[0]]=replace(input,direction)
                input[direction[0]-1]=place_direction(input,[direction[0]-1,direction[1]],"^")
                direction[0]-=1
                # print(input)
        elif guard==">":
            if direction[1]+1>=width:
                break
                return
            next_position=input[direction[0]][direction[1]+1]
            if next_position==obstacle:
                new_direction=turn(guard)
                input[direction[0]]=actually_turn(input[direction[0]],direction[1],new_direction)
            else:
                input[direction[0]]=replace(input,direction)
                input[direction[0]]=place_direction(input,[direction[0],direction[1]+1],">")
                direction[1]+=1
        elif guard=="v":
            if direction[0]+1>=height:
                break
                return
            next_position=input[direction[0]+1][direction[1]]
            if next_position==obstacle:
                new_direction=turn(guard)
                input[direction[0]]=actually_turn(input[direction[0]],direction[1],new_direction)
            else:
                input[direction[0]]=replace(input,direction)
                input[direction[0]+1]=place_direction(input,[direction[0]+1,direction[1]],"v")
                direction[0]+=1
        elif guard=="<":
            if direction[1]-1<0:
                break
                return
            next_position=input[direction[0]][direction[1]-1]
            if next_position==obstacle:
                new_direction=turn(guard)
                input[direction[0]]=actually_turn(input[direction[0]],direction[1],new_direction)
            else:
                input[direction[0]]=replace(input,direction)
                input[direction[0]]=place_direction(input,[direction[0],direction[1]-1],"<")
                direction[1]-=1
traverse(initial_position,input)
count=0
for thing in input:
    for char in thing:
        if char =="X":
            count+=1
print(count)
# EVERYTHING I OFF BY PLUS ONE OUTPUT+1
# shoulda prolly made the input a 2d array for ease of traversing especially for turning direction and actually updating "X" 