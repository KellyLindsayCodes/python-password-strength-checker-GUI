import tkinter as tk

# Password Strength Checker

"""
Project Scope: User is prompted by the terminal to enter in their password. 
Terminal outputs if password is weak, moderate or strong.

The strength of the password is determined by a scoring system.

Factors that influence password strength:
- password contains at least 1 uppercase
- password contains at least 1 lowercase
- password contains at least 1 number 
- password contains at least 1 symbol 
- password length

"""
# First, I will create the function for checking password character types. 
# i.e. (lowercase, uppercase, number, symbol)

def password_strength(password):
    """
    This function checks if the password contains:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one number
    - At least one symbol from the list of symbols

    The score ranges from 0 to 4,
    where each variable met adds 1 to the total score.

    """
    """
    To check if the password contains any of the above, I will use the 
    any() function in combination with an in-built string method. 
    
    The any() function is a built-in Python function. It checks each 
    element of the iterable (like characters in a string). If it finds 
    a True value, it stops and returns True immediately, otherwise if 
    none of the elements are True, it returns False.

    """
    lower_found = any(char.islower() for char in password)
    # This checks for a lowercase letter using the islower() method.
    # islower() is an in-built string method.
    # Each character or char is checked in the password string. 
    # By doing this, I creating a manual list for the alphabet. 


    upper_found = any(char.isupper() for char in password)
    # This checks for the presence of an uppercase letter. 
    # isupper() is an in-built string method. 

    number_found = any(char.isdigit() for char in password)
    # This checks for the presence of a number. 
    # isdigit() is an in-built string method.

    symbols_list = [
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=",
        "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "/", "<",
        ">", "?", "\\", "|"
    ]
    # Symbols do not have an in-built string. 
    # I had to define the list manually.  
    
    symbol_found = any(char in symbols_list for char in password)
    # This checks for a symbol by searching the symbols_list.

    # A sum of the character types is added together to return score. 

    score = lower_found + upper_found + number_found + symbol_found
    
    return score

# Now I will create a function for the password length.  

def evaluate_password_length(password, thresholds=[8, 12, 16, 20]):
    """
    This evaluates the password length and assigns points based on 
    threshold values, i.e if the password has 8 or more characters, it 
    receives a point, if then has 12 or more characters, it receives a 
    point and so on. 

    The function takes the string that is the password and checks it 
    against the list of integers represented in thresholds list. 

    """
    password_length = len(password)
    # This calculates the len or "length" of the password.
    
    length_score = 0
    
    # This checks the password length against each threshold.
    for n in thresholds:
        if password_length >= n:
            length_score += 1  # Adds a point for each threshold met.
    
    return length_score

# Now I will create a function that sums the final score and gives strength rating. 

def check_password_strength():
    """
    This function calculates the password strength and updates the
    result label in the GUI.
    """
    password = password_entry.get()
    if password:
        # this checks if a password is present
        score = password_strength(password)
        length_score = evaluate_password_length(password)
        total_score = score + length_score
        """
        The password length score is add to the character types score
        determined earlier. 
        A final score is reached. 
        """
        
        if total_score < 3:
            strength = 'Weak'
        elif total_score < 5:
            strength = 'Moderate'
        else:
            strength = 'Strong' #rating is determined using an if/else statement. 
        
        result_label.config(text=f"Password strength: {strength}\nScore: {total_score}")

# Basic GUI to illustrate the use of an external library. 
# Creates the main window.
root = tk.Tk()
root.title("Password Strength Checker")

# Set window size. Make window bigger. 
root.geometry("400x400") 

# Add background colour of light blue.
root.configure(bg='lightblue')

# Create and place widgets with styling. 
# This is the CSS for the window. 
# Pady means padding or the space around the box/widget. 
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 18, "bold"), bg='lightblue')
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter your password:", font=("Arial", 14), bg='lightblue')
instruction_label.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 14), width=30)
password_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 14), bg='lightgreen')
check_button.pack(pady=20)

result_label = tk.Label(root, text="Password strength: ", font=("Arial", 14), bg='lightblue')
result_label.pack(pady=10)

root.mainloop()
# This initiates the event loop for the Tkinter application.
# Without this, Tkinter window would not remain open and responsive. 