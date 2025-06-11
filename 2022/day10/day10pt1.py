input="""
noop
noop
addx 6
addx -1
noop
addx 5
addx 3
noop
addx 3
addx -1
addx -13
addx 17
addx 3
addx 3
noop
noop
noop
addx 5
addx 1
noop
addx 4
addx 1
noop
addx -38
addx 5
noop
addx 2
addx 3
noop
addx 2
addx 2
addx 3
addx -2
addx 5
addx 2
addx -18
addx 6
addx 15
addx 5
addx 2
addx -22
noop
noop
addx 30
noop
noop
addx -39
addx 1
addx 19
addx -16
addx 35
addx -28
addx -1
addx 12
addx -8
noop
addx 3
addx 4
noop
addx -3
addx 6
addx 5
addx 2
noop
noop
noop
noop
noop
addx 7
addx -39
noop
noop
addx 5
addx 2
addx 2
addx -1
addx 2
addx 2
addx 5
addx 1
noop
addx 4
addx -13
addx 18
noop
noop
noop
addx 12
addx -9
addx 8
noop
noop
addx -2
addx -36
noop
noop
addx 5
addx 2
addx 3
addx -2
addx 2
addx 2
noop
addx 3
addx 5
addx 2
addx 19
addx -14
noop
addx 2
addx 3
noop
addx -29
addx 34
noop
addx -35
noop
addx -2
addx 2
noop
addx 6
noop
noop
noop
noop
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 1
noop
addx 4
addx -17
addx 18
addx 4
noop
addx 1
addx 4
noop
addx 1
noop
noop

"""
def solution(input):
    instructions = input.strip().split("\n")
    
    X = 1
    X_at_cycle_position = []  # List of X's value during each cycle
    
    for instruction in instructions:
        if instruction == "noop":
            X_at_cycle_position.append(X)  # One cycle, no change
        else:
            value = int(instruction.split()[1])
            X_at_cycle_position.append(X)  # First cycle
            X_at_cycle_position.append(X)  # Second cycle
            X += value                     # Apply effect after two cycles

    # Now pick X's value during these cycles:
    # Cycle numbers are 20, 60, 100, 140, 180, 220 (1-based indexing)
    important_cycles = [20, 60, 100, 140, 180, 220]
    signal_strengths = [X_at_cycle_position[i-1] * i for i in important_cycles]  # i-1 because list is 0-indexed

    return sum(signal_strengths)

# print(solution(input))
print(f"solution: {solution(input)}")
