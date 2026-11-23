

# Writing three initial notes
with open("my_notes.txt", "w") as f:
    f.write("Learn Python.\n")
    f.write("Practice every day.\n")
    f.write("Keep improving.\n")

# Appending the fourth note
with open("my_notes.txt", "a") as f:
    f.write("Never give up learning.\n")

# Reading notes line by line
notes = []

with open("my_notes.txt", "r") as f:
    for line in f:
        notes.append(line.strip())

# Printing the notes and total count
print("--- My notes ---")

for note in notes:
    print(note)

print("Total notes:", len(notes))
