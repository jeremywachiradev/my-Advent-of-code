
pre_input ="""
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
input=pre_input.strip()
def solution(input):
    inputlen=len(input) 

    l,r=0,0
    output=0
    enabled=True

    while l<inputlen:
        if input.startswith("don't()", l):
            print("one dont")
            enabled = False
            l += 7
            continue
        if input.startswith("do()", l):
            print("one do")
            enabled = True
            l += 4
            continue
        # if input[l:l+len("don't()")] == "don't()":
        # if input.startswith("don't()", l):


        # # if input[l:l+7]=="don't()":
        #     l+=7
        #     print("one dont")
        #     enabled=False
        #     continue
        # if input.startswith("do()", l):

        # # if input[l:l+4]=="do()":
        #     print("one do")
        #     enabled=True
        #     l+=4
        #     continue
        
        if input[l:l+4] == "mul(" and enabled:
            bool_val, closing_bracket = isvalidmul(input, l + 3)
            if bool_val:
                multiplied_value = parse_and_multiplymul(input, l + 3, closing_bracket)
                output += multiplied_value
                l = closing_bracket + 1  # move past ")"
                continue
        l += 1
        
    return output
def parse_and_multiplymul(input,opening_bracket,closing_bracket):
    temp_arr=input[opening_bracket+1:closing_bracket].split(",")
    
    return int(temp_arr[0])*int(temp_arr[1])
def isvalidmul(input, r):
    pointer = r + 1
    inputlen = len(input)

    # Parse first number
    while pointer < inputlen and input[pointer].isdigit():
        pointer += 1

    if pointer >= inputlen or input[pointer] != ",":
        return False, pointer

    pointer += 1  # Skip the comma

    # Parse second number
    while pointer < inputlen and input[pointer].isdigit():
        pointer += 1

    if pointer < inputlen and input[pointer] == ")":
        return True, pointer
    return False, pointer        
print(solution(input))