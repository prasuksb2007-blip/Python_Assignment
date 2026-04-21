weight=float(input("Enter the weight of the person (in Kg):"))
height=float(input("Enter the height of the person (in meter):"))
bmi=weight/(height*height)
print(f"The weight of the person is (in Kg)",weight,"and its height is (in meter)",height,".It's BMI is",round(bmi,2))