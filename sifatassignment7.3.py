file_name = "mbox.txt"
sender_list = []

try:
    with open(file_name, "r") as file:
        for line in file:
            if line.startswith("From ") and not line.startswith("From: "):
                sender = line.split()[1]
                sender_list.append(sender)

    for sender in sender_list:
        print(sender)

    print("Number of senders found:", len(sender_list))

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
