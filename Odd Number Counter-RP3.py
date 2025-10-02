e = int(input("Enter a number: "))
sum_of_odd_numbers = 0

print("Odd Numbers", end=" ")
for num in range(1, e + 1):
    if num % 2 == 1:
        sum_of_odd_numbers = sum_of_odd_numbers + num
        print(f"{num}", end=" ")

print(f"\nSum of odd numbers = {sum_of_odd_numbers}")
