
import random
# Adjectives and Nouns for Random usernames
Adjectives=["Perfect","Stylish","Wild","Sweet","Unique","Cool","Brave","Clever"]
Nouns=["Boy","Girl","Star","Captain","Love","Tiger","Dragon"]
#Function to generate username
def generate_username(inc_num,inc_spch):
  username=random.choice(Adjectives)+random.choice(Nouns)
  if inc_num:
    username+=str(random.randint(0,99))
  if inc_spch:
    username+=random.choice(["!","@","#","$","%","_"])
  return username

  #function to save usernames in a file

def save_username(usernames,filename="usernames.txt"):
    try:
      with open(filename,"a") as file:
        for username in usernames:
          file.write(username+"\n")
      print(f"Usernames saved to {filename} successfully!")
    except Exception as e:
      print(f"An error occurred while saving usernames: {e}")

def get_user_preferences():
    inc_num = input("Wanna include numbers in your username? (yes/no): ").strip().lower() == "yes"
    inc_spch = input("Wanna include special characters in your username? (yes/no): ").strip().lower() == "yes"
    num_usernames = int(input("How many usernames would you like to generate? "))
    return inc_num, inc_spch, num_usernames
def main():
       print("WELCOME TO THE RANDOM USERNAME GENERATOR!")
       inc_num = input("Wanna include numbers in your username? (yes/no): ").strip().lower() == "yes"
       inc_spch = input("Wanna include special characters in your username? (yes/no): ").strip().lower() == "yes"
       try:
           num_usernames = int(input("How many usernames would you like to generate? "))
           if num_usernames <= 0:
               raise ValueError("Number of usernames must be greater than 0")
       except ValueError as e:
           print(f"Invalid input: {e} Exit")
           return

       usernames = []
       for _ in range(num_usernames):
           username = generate_username(inc_num, inc_spch)
           usernames.append(username)
       print(f"Generated Usernames: {usernames}")  # Print the list of usernames

       save_option = input("Wanna save these usernames to a file? (yes/no): ").strip().lower()
       if save_option == "yes":
           save_username(usernames)  # Call save_username with the usernames list
           print("THANK YOU")
       else:
           print("THANK YOU")

   # Call the main function

main()