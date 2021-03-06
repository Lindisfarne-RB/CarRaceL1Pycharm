'''Car Racer – in this game users choose a car (numbered one to 6). Then they choose a ‘race distance’
which should be between 5 and 15. A simulated die is rolled and if the car’s number comes up, it
moves forward one space. The winning car is the one which gets to the race distance the first.
Your game should…
● Allow users to choose a car and a distance
● Race the cars. If you are using a text based programming language like Python, it is not
necessary to show each step but the final outcome should be shown and it should be easy
for users to see which car has won.
● Clearly state which car won and give the ‘time’ (ie: number of steps needed).Al
'''


import random

def roll(dist):
    car1, car2, car3, car4, car5, car6 = 0, 0, 0, 0, 0, 0
    car_dist_1,car_dist_2,car_dist_3,car_dist_4,car_dist_5,car_dist_6= 0, 0, 0, 0, 0, 0
    for i in range(1, dist + 1):
        rolling_dice = random.randint(1, 6)
        print("roll....", i, " - ", rolling_dice)
        if rolling_dice == 1:
            car_dist_1 += 1
            car1 +=1
        elif rolling_dice == 2:
            car_dist_2 += 1
            car2 += 1
        elif rolling_dice == 3:
            car_dist_3 += 1
            car3 += 1
        elif rolling_dice == 4:
            car_dist_4 += 1
            car4 += 1
        elif rolling_dice == 5:
            car_dist_5 += 1
            car5 += 1
        elif rolling_dice == 6:
            car_dist_6 += 1
            car6 += 1
        else:
            pass

    listofcars = [car_dist_1, car_dist_2,car_dist_3, car_dist_4, car_dist_5, car_dist_6]
    print("Dist =", listofcars)
    max_value = None
    max_idx = None

    for i   in listofcars:
        if (max_value is None or  i > max_value):
            max_value = i
            max_idx = i

    print('Maximum value:', max_value, "At index: ", max_idx)
    return(max_idx)


car_num=int(input("Enter car num 1-6"))
dist=int(input("Enter distance 5-15"))

winner_car_num=roll(dist)
print("Winner = car ", winner_car_num)