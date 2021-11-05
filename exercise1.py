while True:
    responce = int(input("Enter an integrer: (type 0 to exit program.)  "))
    if responce == 0:
        break
    if responce < 2:
        print("Please enter an integrer bigger than 1.")
        continue
    sum_odds = 0
    sum_even = 0
    even_counter = 0
    for i in range (1, responce+1,2):
        sum_odds += i
    for j in range (2, responce+1,2):
        sum_even += j
        even_counter +=1
    print("- "*10)
    print("Sum of the odd numbers:", sum_odds)
    print("Average of even numbers: ", ((sum_even)/even_counter))
    print("- "*10)