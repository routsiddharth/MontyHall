import random

# CHANGE THE NUMBER OF SIMULATIONS HERE
tries = 1000000

cars = 0

for i in range(tries):

  # Setting up doors. 0 represents goat, 1 represents car
  doors = [0, 0, 0]
  doors[random.randint(0, 2)] = 1

  # Player chooses a door randomly
  choice = random.randint(0, 2)

  # Find out doors which are allowed to be revealed according to the rules
  allowed_doors = [0, 1, 2]

  # Remove chosen door from doors allowed to be revealed
  allowed_doors.remove(choice)

  # Choose a random door to be revealed
  revealed = random.choice(allowed_doors)

  # If the door to be revealed has a car behind it, reveal the other door
  if doors[revealed] == 1:
    allowed_doors.remove(revealed)
    revealed = allowed_doors[0]

  # Choose the unchosen, unrevealed door since the contestant always switches their choice
  for door in [0, 1, 2]:
    if not (door == revealed or door == choice):
      final_choice = door

  if doors[final_choice] == 1:
    cars += 1

