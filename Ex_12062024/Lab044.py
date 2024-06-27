# WAP to calculate and displays the grading for Students
# given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input- score - 89
# output- B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 0-59

# Multiple condition - if, elif, else

# Step 1 -- # Logic Building
# Input ?
# score ->  int
score = int(input("Enter the score\n"))
# output - String -> A,B,C,D,E - string
# Step 2
# Write the rough logic and convert to real one

# score >=90 and score <=100 -> A
# score >=80 and score <=89 -> B
# score >=70 and score <=79 -> C
# score >=60 and score <=69 -> D
# score >=0 and score <=59 -> E


if score >= 90 and score <= 100:
    print("Grade is A")
elif score >= 80 and score <= 89:
    print("grade is B")
elif score >= 70 and score <= 79:
    print("grade is C")
elif score >= 60 and score <= 69:
    print("grade is D")
elif score >= 0 and score <= 59:
    print("grade is E")
else:
    print("Invalid Score")
