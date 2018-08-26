def main():   
    length = int(input("Enter code's length: "))
    formuler(length)
    
def loop():
    while True:
        confirm = input("Wanna break another code with different length? (y/n) ")
        if confirm.lower() == "y" :
            main()
        else :
            print("Bye!")
            break
    
def formuler(length):
    index = []
    result1 = []
    result2 = []
    for n in range(length):
        index.append(n+1)
        result1.append(n)
        result2.append(n+1)
    index[length-1] = 0

    while result1 != result2 :
        result2[0] = result1.count(0)
        for i in index :
            result2[i] = result2.count(i)

        result1[0] = result2.count(0)
        for j in index :
            result1[j] = result1.count(j)
    print("The Da Vinci's code with the length of "+ str(length) + " is", result1, "\n")

print("Welcome to Da Vinci Code Breaker!")
main()
loop()
