# QA  Conditions Exercise
user_mark = int(input("Please enter your mark: " ))
def mark_calculator(mark):
    if mark >= 85:
        return "distinction"
    elif mark >= 65:
        return "Pass"
    else:
        return "Fail"
Result = mark_calculator(user_mark)
print(Result)


