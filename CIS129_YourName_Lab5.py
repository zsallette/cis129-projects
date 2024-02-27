# Module 5 Lab-5
# Zahri Sallette
# February 26,2024
# This program calculates the total number of bottles collected 
# Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = ‘y’	

# Step 2: Loop to run program again
while keepGoing == 'y' :
      	# Step 3: Code to set value of variables
      	totalBottles = 0
        counter = 1
        todayBottles = 0
        totalPayout = 0
# Step 3: getBottles code
      NBR_OF_DAYS = 7
      totalBottles = 0
      todayBottles = 0
      counter = 0

    while counter <= NBR_OF_DAYS:
              today_bottles = int(input())
              total_bottles = total_bottles += todayBottles
              counter = counter + 1

 # Step 5: calcPayout code
    PAYOUT_PER_BOTTLE = 0.10
    total_payout = total_bottles * PAYOUT_PER_BOTTLE

		# code to print the number of total bottles and total payout
		
        print('Do you want to enter another week’s worth of data?')
      	print('Enter y or n')

keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

