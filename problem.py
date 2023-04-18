#list name according to sample program
shoppingCart={}
#Printing the option
print("WELCOME TO THE AMANDO SHOPPING SITE")
print(" 1.Add product to the cart.")
print(" 2.Search the product.")
print(" 3.Delete the product from the cart.")
print(" 4.quit")
Opt=0
#for asking choice everytime
while (Opt!=4):
      
  
  Opt =int(input("Enter your choice : "))
  #ask user how many products they want to add
  if Opt ==1:
      user = int(input("Enter the number of items to be added in the stationary shop : "))
  
      s=0
     
      while(s<user):
        #according to program user can only add 5 items
        #take input from user and print the list according to sample output
        if(user<5):
            B=input("Enter an item:- ")
            c=input("Enter brand name:- ")
            shoppingCart.update({B:c})
            print("you added the following items successfully")
#print the cart is full and list
        else:
          pass
          if(s==0):
           print("cart is full")
        s=s+1
      print(shoppingCart)
  #enter option 2 for searching
  elif Opt ==2:
      A=input("Enter an item:- ")
      k=0
      for i in shoppingCart.keys():
         if(i==A):
           print(i,":",shoppingCart[i])
           k=1
         else:
           pass
      if(k==0):
        print("item not found")
#option 3 for deleting functiion
  elif Opt ==3:
      A=input("Enter an item:-")
      shoppingCart.pop(A)
      print("item deleted successfully")
    

  elif Opt ==4:
    print ("quit")

  else:
    print ("wrong option entered")
