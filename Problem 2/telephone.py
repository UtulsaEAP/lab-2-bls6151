# Name: Braden Stanfield    Class: Wed
def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    print("(" + str((phone_number // 1000000000)) + str((phone_number % 1000000000 // 100000000)) + 
          str(phone_number % 100000000 // 10000000) + ") " + str(phone_number % 10000000 // 1000000) +
          str(phone_number % 1000000 // 100000) + str(phone_number % 100000 // 10000) + "-" + 
          str(phone_number % 10000 // 1000) + str(phone_number % 1000 // 100) + str(phone_number % 100 // 10) +
          str(phone_number % 10 // 1))
if __name__ == "__main__":
    telephone()