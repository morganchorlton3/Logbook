# table of values
# number of pupils   number fo pupils in a team    Number of teams   Number left over
#       154                      5                        31                4
#       187                      5                        37                2
#       129                      5                        25                4

number_of_pupils = int(input('Enter the number of pupils (Total): '))
if number_of_pupils < 0 :
    print('Error please can you enter a correct number of students')
elif number_of_pupils == 0:
    print('The number of pupils can not be 0')
    number_of_pupils = int(input('Enter the number of pupils (Total): '))
else:
    number_of_pupils_in_a_team = 5

    print('Number of pupils: ' , number_of_pupils)
    print('Number of pupils in a Teams: ' , number_of_pupils_in_a_team)
    print(' ')

    number_of_teams = number_of_pupils // number_of_pupils_in_a_team
    print('Number of football teams: ' , number_of_teams)

    number_of_pupils_left_over = number_of_pupils % number_of_pupils_in_a_team
    print('Number of pupils left over: ' , number_of_pupils_left_over)



