#Variables and BMI
#weight = float(input("Enter your weight in kg: "))
#height = float(input("Enter your height in meters: "))
#bmi = weight / (height ** 2)
#print(f"Your BMI is: {bmi:.2f}")

#Type conversion
#age = input("Enter your age: ")
#age_int = int(age)  # Convert the input string to an integer
#age_float = float(age)  # Convert the input string to a float
#is_adult = age_int >= 18  # Check if the user is an adult
#print(f"String: {age} , type: {type(age).__name__}" )
#print(f"Integer: {age_int} , type: {type(age_int).__name__}" )
#print(f"Float: {age_float} , type: {type(age_float).__name__}" )
#print(f"Boolean: {is_adult} , type: {type(is_adult).__name__}" )

#String formatting
name = input("Enter your name: ")
score = int(input("Enter your score: "))
attempts = int(input("Enter the number of attempts: "))
#f-string formatting
print(f"Player: {name}, Score: {score}, Attempts: {attempts}")
#.format() method formatting
print("Player: {}, Score: {}, Attempts:{}".format(name, score, attempts))