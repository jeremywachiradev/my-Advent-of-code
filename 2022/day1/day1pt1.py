input="""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

"""

def solution(input):
    largest_sum=0
    input=input.strip().split("\n")
    current_sum=0
    for val in input:
        if val=="":
            largest_sum=max(largest_sum,current_sum)
            current_sum=0
            continue
        current_sum += int(val)

    return largest_sum

print(solution(input))