block = {0:[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31,36,37,38,39,44,45,46,47,52,53,54,55,60,61,62,63],
            1:[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63],
            2:[32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],
            3:[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63],
            4:[2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,50,51,54,55,58,59,62,63],
            5:[8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31,40,41,42,43,44,45,46,47,56,57,58,59,60,61,62,63]}
found = []
remove = []
number = []
digit = []
possible_answers = []

print("Guess a number between 1 - 63")

b = 0
while b != 6:
    table = f"""    {block[b][0]}   {block[b][1]}   {block[b][2]}   {block[b][3]}   {block[b][4]}   {block[b][5]}   {block[b][6]}   {block[b][7]}
    {block[b][8]}   {block[b][9]}   {block[b][10]}   {block[b][11]}   {block[b][12]}   {block[b][13]}   {block[b][14]}   {block[b][15]}
    {block[b][16]}   {block[b][17]}   {block[b][18]}   {block[b][19]}   {block[b][20]}   {block[b][21]}   {block[b][22]}   {block[b][23]}
    {block[b][24]}   {block[b][25]}   {block[b][26]}   {block[b][27]}   {block[b][28]}   {block[b][29]}   {block[b][30]}   {block[b][31]}"""
    answer = input(f"\n\n{table}\n\nCan your number be found here? Y/n\n>> ").lower()
    
    if answer == "y":
        found.append(b)
        b+=1
    elif answer == "n":
        remove.append(b)
        b+=1
    else:
        print("Incorrect choice.")
        
        


for i in range(len(found)):
    number += block[found[i]]
for i in range(len(remove)):
    digit += block[remove[i]]

x = list(set(number) - set(digit))

for i in range(len(x)):
    possible_answers.append(number.count(x[i]))


correct = x[possible_answers.index(max(possible_answers))]
print(f"Your number is: {correct}")
