def calc_average():
    '''calculate average of eight scores and return average'''
    totalScore = 0
    for i in range(8):
        totalScore += int(input("Please enter score #{}:".format(i+1)))
    avg = totalScore/8 
    return int(avg)
def determine_grade(score):
    '''calculate grade and return value'''
    if 90<=score<=100:
        return "A"
    elif 80<=score<=89:
        return "B"
    elif 70<=score<=79:
        return "C"
    elif 60<=score<=69:
        return "D"
    else:
        return "F"
def main():
    avg = calc_average()
    grade = determine_grade(avg)
    print ("Your average grade is:", grade)
if __name__ == "__main__":
    main()
