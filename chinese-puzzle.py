# 1.	Write a program to solve a classic ancient Chinese puzzle:
#  We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? Hint: use for loop for iterate all possible solutions.
legs=94
heads=35
num_of_rabbits=int(94/4)
num_of_chikens=heads-num_of_rabbits
print(f"number of rabbits are:{num_of_rabbits} and number of chickens are :{num_of_chikens}")

