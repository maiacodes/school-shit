denary = int(input("Input some Denary: "))
binary=""  
while denary>0:  
  #A left shift in binary means /2  
  binary = str(denary%2) + binary  
  denary = denary//2  
print("Your binary number is: " + binary)  