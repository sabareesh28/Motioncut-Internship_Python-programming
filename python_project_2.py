""""

PROJECT-2
         WORD COUNTER
"""

#Function to count words in a given text
def count(text):
  words=text.split()
  return len(words)

#Function to display the Welcome message
def display():
  print("Welcome to Word counter")

#Function to get user input and validate it

def get_user_input():
    while True:
        user_input=input("Please enter a sentence or paragraph.").strip()
        if not user_input:
            print("Invalid input.Please try again")
        else:
            return user_input # Corrected indentation

#Function to display output result
def display_count(word_count):
  print(f"The total number of words in the given text is: {word_count}")
  print("Thank you for using Word counter")

#main program
def main():
  display()
  user_input=get_user_input()
  word_count=count(user_input)
  display_count(word_count)

#Run the program
if __name__ == "__main__":
    main()