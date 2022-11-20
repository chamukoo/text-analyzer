# Programmed by: Lee Anne Y. Angeles
# Lab Exercise 6: Text Analyzer

poem_file = open("Poem.txt", "w")                             # Open file in write mode

poem = """204
A slash of Blue—
A sweep of Gray—
Some scarlet patches on the way,
Compose an Evening Sky—
A little purple—slipped between—
Some Ruby Trousers hurried on—
A Wave of Gold—
A Bank of Day—
This just makes out the Morning Sky."""                               # variable for the poem
poem_file.write(poem + '\n')                                  # Write the string in a text file

count_vowels = 0                                              # Stores the total count of vowels
count_consonants = 0                                          # "                       " consonants
count_digits = 0                                              # "                       " digits
count_special = 0                                             # "                       " special characters

for char in poem:                                             # For statement
    if char.isalpha():                                        # To check\identify whether the characters are alphabet
        if char in 'aeiouAEIOU':                              # To identify whether the alphabet is vowels
            count_vowels += 1                                 # To count the number of vowels
        if char not in 'aeiouAEIOU':                          # To identify whether the alphabet is consonants
            count_consonants += 1                             # To count the number of consonants
        continue
    elif char.isdigit():                                      # To check\identify whether the characters are numbers
        count_digits += 1                                     # To count the numbers of digits
        continue
    else:
        count_special += 1                                    # To count the number of special characters

print("\nNumber of Vowels:", count_vowels)                    # Display the number of vowels
print("Number of Consonants:", count_consonants)              # "                   " consonants
print("Number of Digits:", count_digits)                      # "                   " digits
print("Number of Special Characters:", count_special)         # "                   " special characters
