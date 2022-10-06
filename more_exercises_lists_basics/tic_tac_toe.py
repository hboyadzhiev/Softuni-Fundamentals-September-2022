line_1 = [int(number) for number in input().split()]
line_2 = [int(number) for number in input().split()]
line_3 = [int(number) for number in input().split()]

win_1 = (
        (line_1[0] == line_1[1] == line_1[2] == 1) or
        (line_2[0] == line_2[1] == line_2[2] == 1) or
        (line_3[0] == line_3[1] == line_3[2] == 1) or
        (line_1[0] == line_2[0] == line_3[0] == 1) or
        (line_1[1] == line_2[1] == line_3[1] == 1) or
        (line_1[2] == line_2[2] == line_3[2] == 1) or
        (line_1[0] == line_2[1] == line_3[2] == 1) or
        (line_1[2] == line_2[1] == line_3[0] == 1)

)

win_2 = (
        (line_1[0] == line_1[1] == line_1[2] == 2) or
        (line_2[0] == line_2[1] == line_2[2] == 2) or
        (line_3[0] == line_3[1] == line_3[2] == 2) or
        (line_1[0] == line_2[0] == line_3[0] == 2) or
        (line_1[1] == line_2[1] == line_3[1] == 2) or
        (line_1[2] == line_2[2] == line_3[2] == 2) or
        (line_1[0] == line_2[1] == line_3[2] == 2) or
        (line_1[2] == line_2[1] == line_3[0] == 2)

)

if win_1:
    print("First player won")
elif win_2:
    print("Second player won")
else:
    print("Draw!")