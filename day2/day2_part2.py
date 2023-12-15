

arr = [0, 0, 0] #red, blue, green

def valid(line):
    new_line = line
    new_line = new_line.split(", ")
    for j in new_line:
        #print(j)
        if "red" in j:
            if int(j.split(" red")[0]) > arr[0]:
                arr[0] = int(j.split(" red")[0])
        if "blue" in j:
            if int(j.split(" blue")[0]) > arr[1]:
                arr[1] = int(j.split(" blue")[0])

        if "green" in j:
            #print(int(j.split(" green")[0]))
            if int(j.split(" green")[0]) > arr[2]:
                arr[2] = int(j.split(" green")[0])

    return


with open("input.txt", "r") as f:
    total_sum = 0
    lines = f.readlines()
    #boolean1 = True
    for line in lines:
        game = line.split(": ")
        games = game[1].split("; ")
        for i in games:
            valid(i)
        total_sum += arr[0] * arr[1] * arr[2]
        arr[0] = 0
        arr[1] = 0
        arr[2] = 0
        #if boolean1 == True:
        #    total_sum += int(game[0].split("Game ")[1])
        #    print(int(game[0].split("Game ")[1]))
        #boolean1 = True
        
    print(total_sum)




