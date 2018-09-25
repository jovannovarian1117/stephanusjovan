
# declare data for inputs
# initial velocity set to 0
u = 0
time = 0
velocity_data = 0

# user have to input the time below
t_input = int(input("Input time spent on the road"))

# user have to input their acceleration below
a = int(input("Input acceleration"))

# user have to input distance travel below
s_input = int(input("Input Distance"))
v_limit = 60
distance = 0

# Input text for * explanation
print ("This * indicates every 10 m ! ")

# star loops for distance
star = "*"
star_count = 0
t = 0

while t <= t_input:
    distance = 0.5*a*(t**2)
    velocity_data = a * t_input
    star_count = int(distance/10)
    print ("Duration:" + str(t) + " Distance:" + star*star_count)
    t = t + 1

# data output 1
if velocity_data >= v_limit:
    print("The person went over the speed limit")
    print("Max speed was " + str(v_limit) +"m/s")
else:
    print("The person did not go over the speed limit")
    print("Max speed was " + str(v_limit) +"m/s")

# data output 2
if s_input <= distance:
    print("The person reach the destination")
    print("Reached " + str(distance) + " m")
else:
    print("The person did not reach the destination")
    print("Reached " + str(distance) + " m")







