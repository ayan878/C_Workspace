# initialize last_value to 0
last_value = 0

while True:
    # ask for user input
    input_str = input(f"Enter your calculation (last value: {last_value}): ")

    # check if user wants to exit
    if input_str == "exit":
        break

    # evaluate the input and store the result in last_value
    try:
        result = eval(input_str)
        last_value = result
        print(f"Result: {result}")
    except:
        print("Invalid input. Please try again.")

print("Goodbye!")
