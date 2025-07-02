input="""
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

""".strip().split("\n")
output=0
def recursion(arr,target):
    results={}
    def generate_permutations(index,current_value):
        if index == len(arr):
            results[current_value]=current_value
            return
        # Option 1: Add the next element
        generate_permutations(index + 1, current_value + arr[index])
        # Option 2: Multiply by the next element
        generate_permutations(index + 1, current_value * arr[index])
    generate_permutations(1,arr[0])
    if target in results:
        return True
    return False

       
for line in input:
    values=line.split(":")
    target=int(values[0])
    int_arr=[int(val) for val in values[1].strip().split()]
    
    is_valid=recursion(int_arr,target)
    if is_valid:
        output+=target
print(output)
 
    