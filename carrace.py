import random
car1,car2,car3,car4,car5,car6=0,0,0,0,0,0
car_num=int(input("Enter car num 1-6"))
dist=int(input("Enter distance 5-15"))

for i in range (1 , dist):
    rolling_dice=random.randint(1,6)
    if rolling_dice==1:
        car1+=1

    elif rolling_dice == 2:
        car2 += 1
    elif rolling_dice == 3:
        car3 += 1

    elif rolling_dice == 4:
        car4 += 1
    elif rolling_dice == 5:
        car5 += 1
    elif rolling_dice == 6:
        car6 += 1
    else:
        pass
print(car1,car2,car3,car4,car5,car6)

listofcars=[car1,car2,car3,car4,car5,car6]
print(max(listofcars))