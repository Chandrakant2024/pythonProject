# write a program that calculates and displays the letter grade for a given numerical score e.g A,B,C,D,E based on the following grade scale
#A:90-100
#B:80-89
#C:70-79
#D:60-69
#E:0-59

score = int(input("Enter your scor\n"))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >=50:
    grade = 'E'
else:
    grade ='F'

print('Your letter grade is {grade}')