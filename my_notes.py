# Writing notes to a file
with open("my_notes.txt", "w") as f:
    f.write("My first note.\n")

# Appending another note
with open("my_notes.txt", "a") as f:
    f.write("My second note.\n")

# Reading the notes
with open("my_notes.txt", "r") as f:
    content = f.read()
    print(content)
