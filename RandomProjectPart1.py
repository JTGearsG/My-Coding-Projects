#Passoword Strength Checker

print("\nWelcome To The Password Strength Checker")
user_input = input("Please Enter Your Password ")
password_length = len(user_input)

if password_length >= 10:
    print("Password Strength: Strong")
elif 5 <= password_length < 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")

print(f"Your Password Length is: {password_length}")
print(f"Your Password is: {user_input}")








