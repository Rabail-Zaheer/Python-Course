# Classroom Points Calculator

print("===== Classroom Points Calculator =====")

# Input points for three teams
team1 = int(input("Enter Team 1 points: "))
team2 = int(input("Enter Team 2 points: "))
team3 = int(input("Enter Team 3 points: "))

# Calculate total and average
total_points = team1 + team2 + team3
average_points = total_points / 3

print("\nTotal Points =", total_points)
print("Average Points =", average_points)

# Pack reward stars into boxes
# Each box holds 10 stars
boxes = total_points // 10


print("\nReward Star Packing")
print("Boxes filled =", boxes)

# Compare with last week's score
last_week = int(input("\nEnter last week's total points: "))

if total_points > last_week:
    print("This week's score is higher than last week.")
elif total_points < last_week:
    print("This week's score is lower than last week.")
else:
    print("Both weeks have the same score.")

# Update total using assignment operators
bonus = int(input("\nEnter bonus points: "))
total_points += bonus
print("Total after bonus =", total_points)

penalty = int(input("Enter penalty points: "))
total_points -= penalty
print("Total after penalty =", total_points)

print("\nFinal Total Points =", total_points)
print("===== End of Program =====")