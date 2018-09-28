# Question 4
ball_position = ["real_ball","empty1","empty2"]
function = (input("input A,B,or C to determine the ball's position!"))
for j in function:
    if j == "A":
        ball_position[0] , ball_position[1] = ball_position [1], ball_position[0]
    elif j == "B":
        ball_position[1], ball_position[2] = ball_position [2], ball_position[1]
    else:
        ball_position[0], ball_position[2] = ball_position[2], ball_position[0]
if ball_position.index("real_ball") == 0:
        print ("1")
elif ball_position.index("real_ball") == 1:
        print ("2")
else:
        print ("3")


