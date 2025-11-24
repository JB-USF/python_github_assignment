total_hours = input("Enter total hours studied this week: ")
first_score = input("Enter first test score: ")
second_score = input("Enter second test score: ")
total_hours = float(total_hours)
daily_hours = total_hours / 7
first_score = float(first_score)
second_score = float(second_score)
score_change = second_score - first_score
hour_to_score_ratio = score_change / total_hours
print("Average daily study hours:", daily_hours)
print("Score change per hour studied:", hour_to_score_ratio)
try:
    total_hours= float(total_hours)
    first_score = float(first_score)
    second_score = float(second_score)
except ValueError:
    print("Please enter a valid number and valid test scores.")
    exit()