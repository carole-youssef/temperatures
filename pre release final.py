#Carole Youssef 10.7 4966
#pre release midday and midnight temperatures
#allowing the user to input midday and midnight temps
#finding the total and average of the temperatures
#finding the highest value at midday
#finding the lowest value at midnight

middayTotal=0
midnightTotal=0
highest_mid_temp=0
lowest_night_temp=99
highday=0
lownight=0
day_count=0
day=0
count=0
averageDay=0
averageNight=0

#populating my lists
daytemp = [ ]
nighttemp = [ ]

def Temperatures():
    for count in range(0,1):

#input and store midday and midnight temperatures

        middayTemp=float(input("input midday temp"))

        while middayTemp <0 or middayTemp >100:
            print("error data out of range try again")
            middayTemp=float(input("input midday temp"))
        daytemp.append(middayTemp)

    for count in range(0,1):

        midnightTemp=float(input("input midnight temp"))

        while midnightTemp <0 or midnightTemp >100:
            print("error data out of range try again")
            midnightTemp=float(input("input midnight temp"))
        nighttemp.append(midnightTemp)
           
for day_count in range (1,4):
    day=[day_count]
    print("day",day)
    Temperatures()


print("the elements in the array at midday are",daytemp)
print("the elements in the array at midnight are",nighttemp)


for count in range (0,3):
#finding the total and average temperatures
    middayTotal=middayTotal+daytemp[count]
    midnightTotal=midnightTotal+nighttemp[count]
    count=count+1
    
    averageDay=(middayTotal/count)
    averageNight=(midnightTotal/count)
    
#finding the highest value at midday and the lowest value at midnight
for count in range (0,3):
    if daytemp[count]>highest_mid_temp:
         highest_mid_temp=daytemp[count]

         count=count+1
         highday=count
         
for count in range (0,3):        
    if nighttemp[count]<lowest_night_temp:
         lowest_night_temp=nighttemp[count]
         
         count=count+1
         lownight=count
         
#output of the results
print("the sum of the elements in the array at midday are",middayTotal) 
print("the sum of the elements in the array at midnight are",midnightTotal)
print("the average of the elements in the array at midday is:",averageDay)
print("the average of the elements in the array at midnight is:",averageNight)
print("highest midday value is",highest_mid_temp)
print("lowest midnight value is",lowest_night_temp)
print("the highest midday value was on day",highday)
print("the lowest midnight value was on day",lownight)




