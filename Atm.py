class Atm:
    def _init_(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin 

    def balanceinquiry(self):
        print("Your Balance is: Rupees 1000")

    def cashwithdrawal(self, amount):
        new_amount = 100-amount 
        print("you withdrawed:" + str(amount) +" Your remaining balance is:"+ str(new_amount))  

def main():
    name = input("Hello, what's your name?")
    print("hello,"+ name)
    cardnumber = input("Insert your car number")
    pin = input("Enter your pin") 
    new_user = Atm(cardnumber, pin) 

    print("choose your activity")
    print("1, Balance inquiry")  
    print("2,cashwithdrawal")  
    activity = int(input("enter activity of your choice:"))

    if(activity == 1):
        new_user.balanceinquiry()
    elif (activity == 2):
        amount = int(input("enter the amount:"))
        new_user.cashwithdrawal()
    else:
        print('enter a valid number')    

if __name__ == "__main__" :
    main()      
        