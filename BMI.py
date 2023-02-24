#!/usr/bin/env python
# coding: utf-8

# In[6]:


# input user details 
id = input("Enter your univ ID: ")
name = input("Enter your username : ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

# check if age is within range
if age < 18 or age > 65:
    print("Sorry, this program is only for individuals between the ages of 18 and 65.")
else:
    # convert height from centimeters to meters
    height_m = height / 100

    # calculate BMI
    bmi = weight / (height_m ** 2)

    # determine weight status based on BMI value
    if bmi <= 18.5:
        status = "UNDERWEIGHT"
    elif bmi <= 24.9:
        status = "NORMAL WEIGHT"
    elif bmi <= 29.9:
        status = "OVERWEIGHT"
    else:
        status = "OBESE"

    # print BMI value and weight status
    print(" hello mr " , name , "Your BMI value is " , bmi  ," and you are: " , status )


# In[ ]:




