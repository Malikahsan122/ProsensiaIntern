#Take a sentence input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
words_list = sentence.split()
print("List of words:", words_list)

# Join the list back into a sentence with ' - ' separator
joined_sentence = ' - '.join(words_list)
print("Joined sentence:", joined_sentence)

# Store first and last name in a tuple
name_tuple = ("Malik", "Ahsan")  

# Print each part using indexing
print("First Name:", name_tuple[0])
print("Last Name:", name_tuple[1])
