std = int(input("Enter your mark: "))
if (std >= 50 and std < 60):
    print("Your grade is C+ ")
elif (std >= 60 and std < 70):
    print("Your grade is B")
elif(std >= 70 and std < 80):
    print("Your grade is B+ ")
elif(std >= 80 and std < 90):
    print("Your grade is A")
elif(std >= 90 and std < 100):
    print("Your grade is A+")
else:
    print("Your grade is lower than C+ ")