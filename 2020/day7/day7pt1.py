#MOST UNSOPHISTICATED CODE ESPECIALLY APO CHINI KWA RUNNIGN THE LOOP 100 TIMES YOOH!!!!!

input ="""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip().split("\n")
seen_bags_set=set()
seen_bags=[]
counter=0
for rule in input:
    idx_of_b=0
    for idx,char in enumerate(rule):
        if rule[idx:idx+4]=="bags":
            idx_of_b=idx
            break
    # the o in no is at 14 
    if rule[idx:idx+15]=="bags contain no":
        continue
    bag=rule[0:idx-1]
    # parse for the shiny gold bag 
    
    if "shiny gold bag" in rule[idx:len(rule)]:
        seen_bags_set.add(bag)
        seen_bags.append(bag)
        counter+=1
i=100
while True:
    for rule in input:
        idx_of_b=0
        for idx,char in enumerate(rule):
            if rule[idx:idx+4]=="bags":
                idx_of_b=idx
                break
        if rule[idx:idx+15]=="bags contain no":
            continue
        current_bag=rule[0:idx-1]
            # parse for the other bags
        bag_contents=rule[idx:len(rule)]
        for bag in seen_bags:
            if bag in bag_contents and current_bag not in seen_bags_set:
                seen_bags_set.add(current_bag)
                seen_bags.append(current_bag)      
                break
    i-=1
    if i==0:
        break
# counter=len(seen_bags)
print(len(seen_bags))
print(counter)
