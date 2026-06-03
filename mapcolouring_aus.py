regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

colors = ['Red', 'Green', 'Blue']

adjacency = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'Q': ['NT', 'SA', 'NSW'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

assignment = {}

def is_complete():
    return len(assignment) == len(regions)

def select_unassigned_region():
    for region in regions:
        if region not in assignment:
            return region

def is_safe(region, color):
    for neighbour in adjacency[region]:
        if neighbour in assignment and assignment[neighbour] == color:
            return False
    return True

def solve():
    if is_complete():
        return True

    region = select_unassigned_region()

    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if solve():
                return True

            assignment.pop(region)

    return False

if solve():
    print("Solution Found:\n")
    for region in regions:
        print(region, "->", assignment[region])
else:
    print("No solution exists")
