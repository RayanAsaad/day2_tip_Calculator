bill = input("Cost")
tip = input("hom much do you want to tip")
split = input("how many ways are you spliting the bill")
tip_in_procent = 1 +int(tip)/100
your_part =int(bill) / int(split) * tip_in_procent
your_part1 = round(your_part , 3)
print (your_part1)