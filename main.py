def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n +=1
    return n



def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__=="__main__":
    n=int(input("how many want u:\n"))
    numbers=[]

for i in range(n):
    number=int(input("entr the no:\n"))
    numbers.append(number)

for i in range(n):
    print(
          f"nxt palindrome for {numbers[i]}is {next_palindrome(numbers[i])}")
