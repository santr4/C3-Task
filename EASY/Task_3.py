# ** colour classifier

# ** Task description: 
'''

One fine day, Shri Ram’s Guru gave everyone to find three different colours flags while hunting in the mountains during one of the Vidya-Grehan sessions. 
While hunting one of his friends reveals that he is Color Blind and thus is unable to find the colors of the flag he had to find. 
Help Shri Ram classify these colours.

'''

# ** Task details:
'''

Create a Python Script that can classify colours: Red, Blue and Green.
You can approach this task by using a set of colour ranges for each category and
then using simple if-else statements to determine the colour category based on the RGB values of the input colour.

'''
# ** I have solved this question using dictionaries.

Red = {12800:'maroon',1783434:'firebrick',2559971:'tomato'}

Blue = {2525112:'midnight blue',10128:'navy',65105225:'royal blue'}

Green = {4613987:'sea green',11000:'dark green',1281280:'Olive'}

print("enter the number of flags that are to be identified by Shri Ram in the Vidya-Grehan sessions: ")
n = int(input())

for i in range(n):
    print("enter the rgb value of the color of the flag: ")
    rgb = int(input())
    for i in Red.keys():
        if(rgb == i):
            print("color of the flag is red")
    for j in Blue.keys():
        if(rgb == j):
            print("color of the flag is blue")
    for k in Green.keys():
        if(rgb == k):
            print("color of the flag is green")
    
        