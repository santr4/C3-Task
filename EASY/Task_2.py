# ** Guess the Number
# ** Task Description
'''
Shri Ram once saw a Yodha, expressing his Sastra-Vidya. He found it very intriguing, so he asked his Guru about it. He said, “Sastra-Vidya is the expression of one’s self through their Sastra. It’s an art with intricate body movements creating profound patterns depicting their experience and love for their Sastra.” Shri Ram now even more intrigued, started looking into these so-called patterns mentioned by his Guru.
Help Shri Ram solve such patterns.

'''

# ** Task details
'''
Create a Simple Pattern Recogniser in Python.
The script will take in a string with any list input.
The script will detect some simple repeating patterns from it and print “Pattern Found” and then the pattern that is found, else “Pattern Not Found”.
The script will also print the number of times the pattern repeats in the string.
Example:
Input:

[1,2,3,1,2,3,1,2,3,1,2,3]
Output:

Pattern Found: [1,2,3]
Number of times the pattern repeats: 4
Input:

[1,2,3,4,5,6,7,8,9,10]
Output:

Pattern Not Found

'''

# ** code -->


print("enter the elements of a list")   # ** first we will enter the elements of the list/array
input_string = input()

input1 = input_string.split()   # ** using the .split() function we split the elements into a collection of strings in the array.
print(input1)

list_to_string = ''.join([str(ele) for ele in input1])   # ** now we will join back the characters in the array into a string which is beneficial for us only.
print(list_to_string)
print(type(list_to_string))

def pattern(string):
    l = len(string)
    
    for i in range(1, l // 2 + 1):
        pattern = string[:i]
        count = string.count(pattern)  # ** function to count the frequency of substring in the main string
        
        if count >= 2 and pattern * count == string: 
            print("pattern found")
            print("therefore the pattern is: " + str(pattern))
            print("the frequency of the pattern is: " + str(count))
            return
    print("pattern not found")
    
pattern(list_to_string)