
alpha = []
charlie = []
golf = []
quebec = []
romeo = []
anomalous = []
total_all_messages = []

char = ''

with open('data.txt') as f:
    lines = f.readlines()

    for char in lines:
        if char[5] == "A":
            alpha.append(char)
            print(len(alpha))
        elif char[5] == "C":
            charlie.append(char)
            print("The total number of charlie messages is: " + str(len(charlie)))
        elif char[5] == "G":
            golf.append(char)
            print("The total number of golf messages is: " + str(len(golf)))
        elif char[5] == "Q":
            quebec.append(char)
            print("The total number of quebec messages is: " + str(len(quebec)))
        elif char[5] == "R":
            romeo.append(char)
            print("The total number of romeo messages is: " + str(len(romeo)))
        else:
            anomalous.append(char)
            print("The total number of anomalous messages is: " + str(len(anomalous)))        

    for line in lines:
        total_all_messages.append(line)
        print("The total number of all messages is: " + str(len(total_all_messages)))
