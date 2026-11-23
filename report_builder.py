import csv

total = 0
passed = 0
failed = 0
rows = []

try:
    with open("hubs.csv", "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        score = int(row["score"])
        total += score

        if score >= 50:
            passed += 1
        else:
            failed += 1

    average = round(total / len(rows), 1)

    with open("report.txt", "w") as f:
        f.write("LEARNER REPORT\n")
        f.write("Total learners: " + str(len(rows)) + "\n")
        f.write("Passed: " + str(passed) + "\n")
        f.write("Failed: " + str(failed) + "\n")
        f.write("Average score: " + str(average) + "\n")

    print("Report written to report.txt")

except FileNotFoundError:
    print("hubs.csv not found")