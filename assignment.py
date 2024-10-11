def calc_average():
    #calculate the average of eight scores and return average
    total_score = 0
    for i in range(8):
        total_score += int(input("Please enter score #{}: ".format(i+1)))
    avg = total_score/8
    return int(avg)

def determine_grade(score):
    #calculate grade and return value
    if 90 <= score <= 100:
        return "A"

    if 80 <= score <= 89:
        return "B"

    if 70 <= score <= 79:
        return "C"

    if 60 <= score <= 69:
        return "D"

    else:
        return "F"

def main():
    avg = calc_average()
    grade = determine_grade(avg)
    print ("Your average grade is:", grade)

if __name__=="__main__":
    main()
