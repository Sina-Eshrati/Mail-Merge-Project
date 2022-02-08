with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()
with open("./Input/Letters/starting_letter.txt") as data:
    template = data.read()

new_names = []
for name in names:
    new_names.append(name.strip())


def write_letter(name):
    invitation_letter = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(invitation_letter)


for name in new_names:
    write_letter(name)
