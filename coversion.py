print("How many kilometers did you drive?")                       #Question:

kms = input()                                                     #Conversion:
miles = float(kms) / 1.60934

if miles > 15:                                                    #Condition:
    print("Error")
elif miles < 15:
    print("Error")
    
print("How many kilograms do you weight?")                        #Question:

kilogram = input()                                                #Conversion:
gram = float(kilogram) * 1000

if gram > 100000:                                                 #Condition:
    print("Error")
elif gram < 100000:
    print(f"your weight is {gram} g")




