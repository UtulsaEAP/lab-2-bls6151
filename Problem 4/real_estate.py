# Name: Braden Stanfield    Class: Wed
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    dif = current_price - last_month_price
    mort = (current_price * 0.051) /12
    print("This house is $" + str(current_price) + ". The change is $" + str(dif) + " since last month.")
    print("The estimated monthly mortgage is $" + (f'{mort:.2f}') + ".")
    
if __name__ == "__main__":
    real_estate()