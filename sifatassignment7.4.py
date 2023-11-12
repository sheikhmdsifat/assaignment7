num_list = []

while True:
    user_input = input("Enter an integer or 'done' to finish: ")
    
    if user_input == 'done':
        break
    
    try:
        num = int(user_input)
        num_list.append(num)
        average = sum(num_list) / len(num_list)
        print("Average:", average)
    except ValueError:
        print("Invalid input. Please enter an integer or 'done'.")

print("Program finished.")
