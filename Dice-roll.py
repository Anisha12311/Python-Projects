import random
def parse_input(value):
    options = {"1","2","3","4","5","6"}
    
    if value.strip() in options:
        return int(value)    
    else :
        return f"{value.strip() } is invalid. Please choose between 1 to 6"
    

def dice_roll(num_dice):
    
    roll_results = []
    
    for _ in range(num_dice):
        roll = random.randint(1,6)
        roll_results.append(roll)    
    
    return roll_results



DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}




DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])


def dice_roll_face(dice_values):
    
    dice_faces = []
    
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    
    dice_faces_row = []
    
    for rowIdx in range(DIE_HEIGHT):
        
        dice_component = []
        
        for dice in dice_faces:
            
            dice_component.append(dice[rowIdx])
        row_string = " ".join(dice_component)  
        dice_faces_row.append(row_string) 
    dice_faces_diagram = "\n".join(dice_faces_row)
    return dice_faces_diagram


user_input = input("How many dice do you want to roll? (1 to 6) ")

num_dice = parse_input(user_input)


dice_values = dice_roll(num_dice)

result = dice_roll_face(dice_values)


print(result)