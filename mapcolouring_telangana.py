districts = [
    "Adilabad","Bhadradri_Kothagudem","Hyderabad","Jagtial","Jangaon",
    "Jayashankar_Bhupalpally","Jogulamba_Gadwal","Kamareddy","Karimnagar",
    "Khammam","Kumuram_Bheem","Mahabubabad","Mahabubnagar","Mancherial",
    "Medak","Medchal","Mulugu","Nagarkurnool","Nalgonda","Narayanpet",
    "Nirmal","Nizamabad","Peddapalli","Rajanna_Sircilla","Rangareddy",
    "Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy",
    "Warangal_Rural","Warangal_Urban","Yadadri_Bhongir"
]

adjacent_districts = {
    "Adilabad": ["Kumuram_Bheem","Nirmal","Mancherial"],
    "Kumuram_Bheem": ["Adilabad","Mancherial"],
    "Mancherial": ["Adilabad","Kumuram_Bheem","Peddapalli","Nirmal"],
    "Nirmal": ["Adilabad","Mancherial","Jagtial"],
    "Jagtial": ["Nirmal","Karimnagar","Rajanna_Sircilla","Nizamabad"],
    "Rajanna_Sircilla": ["Karimnagar","Jagtial"],
    "Karimnagar": ["Peddapalli","Jagtial","Rajanna_Sircilla","Warangal_Urban"],
    "Peddapalli": ["Mancherial","Karimnagar","Warangal_Urban"],
    "Nizamabad": ["Jagtial","Kamareddy"],
    "Kamareddy": ["Nizamabad","Medak","Siddipet"],
    "Medak": ["Kamareddy","Sangareddy","Siddipet"],
    "Sangareddy": ["Medak","Rangareddy","Vikarabad","Medchal"],
    "Medchal": ["Hyderabad","Rangareddy","Sangareddy"],
    "Hyderabad": ["Medchal","Rangareddy"],
    "Rangareddy": ["Hyderabad","Medchal","Sangareddy","Vikarabad","Mahabubnagar"],
    "Vikarabad": ["Sangareddy","Rangareddy","Mahabubnagar"],
    "Mahabubnagar": ["Rangareddy","Vikarabad","Narayanpet","Wanaparthy","Jogulamba_Gadwal"],
    "Narayanpet": ["Mahabubnagar"],
    "Jogulamba_Gadwal": ["Mahabubnagar","Wanaparthy"],
    "Wanaparthy": ["Mahabubnagar","Nagarkurnool","Jogulamba_Gadwal"],
    "Nagarkurnool": ["Wanaparthy","Nalgonda"],
    "Nalgonda": ["Nagarkurnool","Suryapet","Yadadri_Bhongir"],
    "Yadadri_Bhongir": ["Nalgonda","Siddipet"],
    "Siddipet": ["Medak","Kamareddy","Yadadri_Bhongir","Jangaon"],
    "Jangaon": ["Siddipet","Warangal_Rural"],
    "Warangal_Rural": ["Jangaon","Warangal_Urban","Mahabubabad"],
    "Warangal_Urban": ["Warangal_Rural","Karimnagar","Peddapalli","Mulugu"],
    "Mulugu": ["Warangal_Urban","Jayashankar_Bhupalpally"],
    "Jayashankar_Bhupalpally": ["Mulugu"],
    "Mahabubabad": ["Warangal_Rural","Khammam"],
    "Khammam": ["Mahabubabad","Bhadradri_Kothagudem","Suryapet"],
    "Bhadradri_Kothagudem": ["Khammam"],
    "Suryapet": ["Nalgonda","Khammam"]
}

available_colors = ["Red", "Green", "Blue", "Yellow"]

solution = {}

def completed():
    return len(solution) == len(districts)

def choose_district():
    for district in districts:
        if district not in solution:
            return district
    return None

def can_assign(district, color):
    for neighbour in adjacent_districts.get(district, []):
        if solution.get(neighbour) == color:
            return False
    return True

def map_coloring():
    if completed():
        return True

    current_district = choose_district()

    for color in available_colors:
        if can_assign(current_district, color):
            solution[current_district] = color

            if map_coloring():
                return True

            solution.pop(current_district)

    return False

if map_coloring():
    print("Telangana Map Coloring Solution:\n")
    for district in districts:
        print(district, "->", solution[district])
else:
    print("No solution found")
