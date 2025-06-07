import string


input="""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

"""
def solution(input):
    input=input.strip().split()
    common_char=[]
    output=0

    for input in input:
        left_start_index=len(input)//2
        my_list=[]
        for i in range(left_start_index):
            my_list.append(input[i])
        
        for i in range(left_start_index,len(input)):
            
            if input[i] in my_list:
                common_char.append(input[i])
                break
    for char in common_char:
        output+=get_value(char)

    return output
def get_value(char):
    
    value_map=create_char_to_int_map_concise()
    return value_map[char]

    

def create_char_to_int_map_concise():
    char_map = {}
    value = 1

    # Loop through lowercase letters
    for char in string.ascii_lowercase:
        char_map[char] = value
        value += 1

    # Loop through uppercase letters
    for char in string.ascii_uppercase:
        char_map[char] = value
        value += 1

    return char_map

print(solution(input))