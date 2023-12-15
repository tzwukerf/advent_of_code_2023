
with open("input.txt", "r") as f:
    final_sum = 0;
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    index1 = 100
    index2 = -1
    first_dig = -1
    second_dig = -1
    lines = f.readlines();
    for line in lines:
        for i in range(len(arr)):
            if arr[i] in line:
                if line.find(arr[i]) < index1:
                    index1 = line.find(arr[i])
                    first_dig = i
                if line.rfind(arr[i]) > index2:
                    index2 = line.rfind(arr[i])
                    second_dig = i
                    
        for i, c in enumerate(line):
            if c.isdigit() and i < index1:
                index1 = i
                first_dig = int(c)
                break
        #reverse = line[::-1]
        for i, c in enumerate(line):
            if c.isdigit() and i > index2:
                index2 = i
                second_dig = int(c)
                #break
        final_sum += first_dig * 10 + second_dig
        #rint(first_dig * 10 + second_dig)
        first_dig = -1
        second_dig = -2
        index1 = 100
        index2 = -1

    print(final_sum)
    f.close()






