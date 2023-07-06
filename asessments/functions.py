def say_hello():
    return 'Hello'
    
hello = say_hello()

print(hello)


def even_check(num):
    return num % 2 == 0


isEven = even_check(3)

def check_even_list(num_list):
    
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
numbers = [1,3,5]
check_even_list(numbers)