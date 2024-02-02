
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    after6 = caffeine_mg /2
    after12 = caffeine_mg /4
    after24 = caffeine_mg /8
    print("After 6 hours: " + f'{after6:.2f}' + " mg")
    print("After 12 hours: " +f'{after12:.2f}'+ " mg")
    print("After 24 hours: " +f'{after24:.2f}'+ " mg")
if __name__ == "__main__":
    caffeine()