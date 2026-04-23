import time


print("Welcome to expense splitter!")


while True:
    try:
        total_bill = float(input("Enter the total bill amount: "+"$"))
        if total_bill < 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid Error. Please enter a valid number.")


people = []
while True:
    name= input(("Enter the name of perticipant (or type done to finish): ")).lower().strip()
    if name == "done":
        if len(people) < 2:
            print("please enter at least 2 participants. ")
            continue
        break
    elif name.strip() == "":
        print("Name cannot be empty, please enter a valid name.")
    elif not name.isalpha():
        print("Name can only contain letters, please enter a valid name.")
    elif name in people:
        print("This name already exists, please enter a different name.")
    else:
        people.append(name)
# 3. Split logic
print('3. Now, specify the percentage each person will pay.')
print('(Type "even" at any time to split the bill equally.)')

people_dict = {}
total_percentage = 100
even = False
while True:
    print("Do you want to split the bill evenly? (yes/no): ")
    response = input().lower()
    if response == "yes":
        even = True
        equal_split = total_bill / len(people)
        for person in people:
            people_dict[person] = equal_split
        break
    elif response == "no":
        for i ,person  in enumerate(people):
            
            if i == len(people) -1:
                print(f"{person.capitalize()} will take the remaining {total_percentage:.0f}%.")
                people_dict[person] = (total_percentage/100) * total_bill
                
                total_percentage = 0
                
                time.sleep(1)  
                break


            while True:
                try:
                    percentage = float(input(f"Enter the percentage for {person }(remaaning {total_percentage:.0f}%): "))
                    if  percentage < 0 or percentage > total_percentage:
                        print(f"please enter a vaild percntage between 0 and {total_percentage:.0f}")
                    else:
                        people_dict[person] = (percentage / 100) * total_bill
                        total_percentage -= percentage
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        break
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        continue
    
   


if even:
    print("\nThe bill will be split evenly among the participants.")
else:
    print("\nThe bill will be split based on the specified percentages.")





print("----------------------------------------")
print("--- split summary ---")
for person, amount in people_dict.items():
    print(f"{person.capitalize():10}: ${amount:.2f}")
print("----------------------------------------")