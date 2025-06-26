input ="""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

""".strip().split()
def solution(input):
    count=0
    for  word_index,word in enumerate(input):
        for char_index,char in enumerate(word):
            if char=="X":
                count+=isValidCount(input,word_index,char_index)
    print(count)           


def isValidCount(input,word_index,char_index):
    count=0
    # HORIZONTAL
    # check to the left XMAS 
    if char_index+4<=len(input[word_index]):
        if input[word_index][char_index:char_index+4]=="XMAS":
            count+=1
    # check to the right SAMX 
    if char_index-3>=0:
        if input[word_index][char_index-3:char_index+1]=="SAMX":
            count+=1
    # VERTICAL
    # check to vertical down XMAS 
    if word_index+3<len(input):
        if input[word_index+1][char_index]=="M" and input[word_index+2][char_index]=="A"and input[word_index+3][char_index]=="S":
            count+=1
        # check diagonal right down 
        if char_index+3<len(input[word_index]):
            if input[word_index+1][char_index+1]=="M" and input[word_index+2][char_index+2]=="A"and input[word_index+3][char_index+3]=="S":
                count+=1
        # check diagonal left down 
        if char_index-3>=0:
            if input[word_index+1][char_index-1]=="M" and input[word_index+2][char_index-2]=="A"and input[word_index+3][char_index-3]=="S":
                count+=1  
    # check to vertical up XMAS 
    if word_index-3>=0:
        if input[word_index-1][char_index]=="M" and input[word_index-2][char_index]=="A"and input[word_index-3][char_index]=="S":
            count+=1
        # check diagonal right up 
        if char_index+3<=len(input[word_index]):
            if input[word_index-1][char_index+1]=="M" and input[word_index-2][char_index+2]=="A"and input[word_index-3][char_index+3]=="S":
                count+=1
        # check diagonal left up 
        if char_index-3>=0:
            if input[word_index-1][char_index-1]=="M" and input[word_index-2][char_index-2]=="A"and input[word_index-3][char_index-3]=="S":
                count+=1    
    return count

solution(input)