with open("abc.txt","r") as file:
    # data = file.read()
    # data = file.readline()
    data = file.readlines()[-1]
    print(data)