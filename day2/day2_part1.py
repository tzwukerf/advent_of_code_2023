

def valid(line):
    boolean = True
    new_line = line
    new_line = new_line.split(", ")
    for j in new_line:
        #print(j)
        if "red" in j:
            if int(j.split(" red")[0]) > 12:
                boolean = False
                break
        if "blue" in j:
            if int(j.split(" blue")[0]) > 14:
                boolean = False
                break
        if "green" in j:
            #print(int(j.split(" green")[0]))
            if int(j.split(" green")[0]) > 13:
                boolean = False
                #print(boolean)
                break
    return boolean


with open("input.txt", "r") as f:
    total_sum = 0
    lines = f.readlines()
    boolean1 = True
    for line in lines:
        game = line.split(": ")
        games = game[1].split("; ")
        for i in games:
            if valid(i) == False:
                boolean1 = False
                break
        if boolean1 == True:
            total_sum += int(game[0].split("Game ")[1])
            #print(int(game[0].split("Game ")[1]))
        boolean1 = True
        
    print(total_sum)




