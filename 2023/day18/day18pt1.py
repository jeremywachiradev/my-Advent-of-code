"""
WRONG   WRONG !!!!!!!!!!!!
"""

input="""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
""".strip().split("\n")
starting=(1,1)
trenches=[]
trenches.append([starting,starting])
output=0

max_row=0
max_col=0
def traverse(starting,direction,steps):
    rows=starting[0]
    cols=starting[1]
    if direction =="U":
        first_step=(rows-1,cols)    
        last_step=(rows-steps,cols)
    elif direction=="D" :
        first_step=(rows+1,cols)  
        last_step=(rows+steps,cols)
    elif direction=="L" :
        first_step=(rows,cols-1)
        last_step=(rows,cols-steps)
    elif direction=="R" :
        first_step=(rows,cols+1)
        last_step=(rows,cols+steps)
    
    if first_step!=last_step:
        trenches.append([first_step,last_step])
        
    else:
        trenches.append([last_step])
    return last_step[0],last_step[1]
   
for line in input:
    all=line.split()
    direction=all[0]
    steps=int(all[1])
    # print(all,steps,direction)
    row,col=traverse(trenches[-1][-1],direction,steps)
    max_row=max(row,max_row)
    max_col=max(col,max_col)
    # print(f"the direction is {direction}and the steps is {steps}")

trenches_map=[["." for _ in range(max_col+2) ]for _ in range(max_row+2)]

# print(trenches)

for index,element in enumerate(trenches):
    if index==0:
        continue
    # print(element)
    starting_row=(element[0][0])
    starting_col=(element[0][1])
    if len(element)==1:
        ending_col=starting_col
        ending_row=starting_row
    else:
        ending_row=(element[1][0])
        ending_col=(element[1][1])
    row_diff=ending_row-starting_row
    col_diff=ending_col-starting_col
    is_positive=False
    if row_diff==0:
        
        if col_diff>0:
            is_positive=True
        while True:
            trenches_map[starting_row][starting_col]="#"
            # print(starting_col,type(starting_col))
            # print(f"starting row is {starting_row} and starting col is {starting_col}")
            if starting_col==ending_col:
                break
            if is_positive:
                starting_col+=1
            else:
                starting_col-=1
                    
        
    elif col_diff==0:
        if row_diff>0:
            is_positive=True
        while True:
            trenches_map[starting_row][starting_col]="#" # print(f"starting row is {starting_row} and starting col is {starting_col}")
            
            if starting_row==ending_row:
                break
            if is_positive:
                starting_row+=1
            else:
                starting_row-=1
    
from collections import deque

# Flood fill from (0,0)
def flood_fill(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    queue.append((start_r, start_c))

    while queue:
        r, c = queue.popleft()
        if r < 0 or r >= rows or c < 0 or c >= cols:
            continue
        if grid[r][c] != ".":
            continue
        grid[r][c] = "O"  # Temporarily mark as outside
        queue.append((r+1, c))
        queue.append((r-1, c))
        queue.append((r, c+1))
        queue.append((r, c-1))

# Run the fill
flood_fill(trenches_map, 0, 0)

for r in range(len(trenches_map)):
    for c in range(len(trenches_map[0])):
        if trenches_map[r][c]=="." or trenches_map[r][c]=="#":
            output+=1

print(output)
print(trenches_map)
print(max_row,max_col)
