user_name = input("Enter your name (minimum 3 characters): ")

if len(user_name) < 3:
    print("User name must have at least 3 characters.")
else:
    greeting = "Hello <<UserName>>, How are you?"
    greeting_with_name = greeting.replace("<<UserName>>", user_name)
    print(greeting_with_name)