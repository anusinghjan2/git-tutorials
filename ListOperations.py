if __name__ == '__main__':
    N = int(input())
    lst = []

    for i in range(N):
        input1 = input("enter an operation:").strip().split(" ")

        if input1[0] == "append":
            lst.append(input1[1])
        elif input1[0] == "print":
            print(input1[1])
        elif input1[0] == "remove":
            lst.remove(input[1])
        elif input1[0] == "insert":
            lst.insert(int(input1[1]),input1[2])
        elif input1[0] == "sort":
            lst.sort()
        elif input1[0] == "pop":
            lst.pop()
        elif input1[0] == "reverse":
            lst.reverse()
        else:
            print("!!Operation not supported!!")

print("added new line from github")



    
