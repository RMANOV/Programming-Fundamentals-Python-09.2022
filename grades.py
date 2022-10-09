

def grades_in_words(grade):
    if grade >= 5.5:
        return 'Excellent'
    elif 4.5 < grade <= 5.49:
        return 'Very Good'
    elif 3.5 < grade <= 4.49:
        return 'Good'
    elif 3 < grade <= 3.49:
        return 'Poor'
    else:
        return 'Fail'



#   2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"






grades = float(input())
print(grades_in_words(grades))
