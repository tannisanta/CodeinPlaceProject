# Code in Place projects

I had two ideas for projects and decided to leave both of them.

## Mood Checker 

### Idea

Start the user's day positively by acknowledging their mood and offering a relevant quote or message to uplift their spirits or celebrate their happiness. 
The purpose is to provide a simple yet thoughtful interaction that can potentially improve the user's mindset and overall well-being.

### Use case

The primary use case for this project is to serve as a morning routine or daily ritual for individuals who value self-reflection and desire a positive start to their day. 
It can be particularly useful for those who find comfort in inspirational quotes or motivational messages, especially during challenging times. 
I am a fan of quotes and I believe they are small pieces of wisdom that connect us as humans.

### How it works

This script enhances the user's mood by providing personalized quotes. It reads quotes from two text files: one for positive moods (happy or okay) and another for negative moods (sad). 
After prompting the user to input their current mood, the script randomly selects and displays a relevant quote from the corresponding file, offering a tailored, uplifting message to the user.

### Things out of scope

- Mood tracking over time.
- Personalization that is based on user preferences or specific circumstances
- Customization options for adding, changing, or removing the quotes from files.

While the Mood Checker project is relatively simple, it could serve as a starting point for more advanced projects or it can be slightly improved for self-reflection purposes.

## Password Storage project

### Idea

The project aims to provide a convenient way for users, who frequently test different platforms and have multiple test accounts, to store their passwords. 
The main idea behind this project is to simplify the process of generating, storing, and retrieving passwords for test accounts or other accounts that do not require a high level of security. 

### Use case

As a technical writer, I often test different platforms, have multiple test accounts, and store many manually created passwords in a file. 
My idea was to create a useful program to help me generate and store passwords for test accounts or other accounts I don’t bother to secure. I use 2FA for important accounts. :wink: 
I would save all these passwords in a file regularly synced to my cloud storage so I can access it from any device.

### How it works

The script allows the user to generate secure passwords based on specified criteria - length, inclusion of uppercase, lowercase, numbers, and symbols. 
After generating the password, the user sees a prompt to save it under a keyword. The script checks for duplicate keywords before saving the new password-keyword pair to a file.

Alternatively, the user can view either a specific password by entering its associated keyword or all stored passwords.

After adding a new password, the script displays the current number of passwords stored in the file. The user can exit the program cleanly after adding or viewing passwords.

### Things out of scope

- Input validation for password generation
- Safeguarding access to the program with a password
- Excluding specific symbols from the password generation process
  
I believe this project serves as a simple yet efficient solution for individuals who need to generate secure passwords, associate them with memorable keywords, and store them in a centralized location, allowing easy access from anywhere for managing test accounts or accounts that do not require robust security measures.
