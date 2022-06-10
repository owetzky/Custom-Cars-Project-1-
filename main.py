# Ask at least 6 questions 
# At least one multiple choice, one yes/no, one short answer
# Summary section at the end 
# Each question/response shopuld be one single line
# Use "===" to separate sections 
# Questions and rsponses should be easy to read

print("==========================================")
print("Welcome to the UMBC Car Customiztion Form!")
print("==========================================")
print()
# Question 1 (multiple choice question)
print("*For multiple choice questions, please enter the corresponding letter!*")
print()
print("1. Vehicle Model: What vehicle model would you like to order?")
print()
print("a. Tesla Cybertruck")
print("b. Rivian R1T")
print("c. Ford F-150 Lightening")
print("d. GMC Hummer EV")
print()
vehicleType = input("Please enter a selection (a, b, c or d): ")
print()
print()

# Question 2 (yes/no question)
print("2. Vehicle Package: Would you like the premium package?")
vehiclePackage = input("Please enter 'yes' or 'no': ")
print()
print()

# Question 3 (short answer question)
vehicleColor = input("3. Vehicle Color: What color would you like the vehicle? ")
print()
print()

# Question 4 (short answer question)
creditScore = input("4. Credit Score: What is your credit score? ")
print()
print()

# Question 5 (yes/no question)
print("5. Vehicle Trade-in: Do you have a vehicle to trade-in?")
vehicleTradeIn = input("Please enter 'yes' or 'no': ")
print()
print()

# Question 6 
print("1. Vehicle Battery Size: What vehicle battery size would you like?")
print()
print("a. 75 kWh")
print("b. 100 kWh")
print("c. 150 kWh")
print("d. 200 kWh")
print()
vehicleBatterySize = input("Please enter a selection (a, b, c or d): ")
print()
print()

print("==========================================")
print("Order Summary:")
print()
print(f"1. Vehicle Model: {vehicleType})")
print(f"2. Vehicle Package: {vehiclePackage})")
print(f"3. Vehicle Color: {vehicleColor}")
print(f"4. Credit Score: {creditScore})")
print(f"5. Vehicle Trade-in: {vehicleTradeIn})")
print(f"6. Vehicle Model: {vehicleBatterySize}")
print()
print()
print("Thank You for your order!")