def check_even_odd(number):
   if number % 2==0:
       return "the number is even."
   else:
       return "the number is odd."
   
def main():
    #ask the user for a number
    num = int(input("Enter a number: "))
       
    message =check_even_odd(num)

    #print the result 
    print(message)

       #run the main function 
if __name__ == "__main__":
    main()