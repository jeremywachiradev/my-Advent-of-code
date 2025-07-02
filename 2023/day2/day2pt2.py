input="""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

""".strip().split("\n")

output=0
for line in input:
    game=line.split(":")
    color_map={
        "green":0,
        "red":0,
        "blue":0
    }
    # green=0
    # red=0
    # blue=0
    sets=game[1].strip().split(";")
    for entry in sets:
        hand=entry.strip().split(",")
        for sub_hand in hand:
            stripped=sub_hand.strip().split()
            value=int(stripped[0])
            color=stripped[1]
            if color_map[color]<value:
                color_map[color]=value
    output+=color_map["red"]*color_map["green"]*color_map["blue"]
    
                
print(output)
