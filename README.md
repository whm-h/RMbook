# RMBook
Encryption of words and numbers with Python
Hello, thank you for choosing us
This library is for small word encryption.
If you're looking for fast and scalable cryptography up to high sentence counts, check out the Bynerlock library on my GitHub page.
https://github.com/whm-h/Bynerlock

But if you want special encryption, this library is suitable for you

# Lock file
To encrypt, you must use the following command
RM.Lock(your_text , name = 'Custom_name_to_save_the_file_key_to_that_name' , Protocol = S1 Until S9)

# Protocol
Protocol => Type of random encryption based on letters and numbers
The higher the protocol number, the harder the encryption type and the longer it takes, choose from 1 to 10 encryption types according to your needs.
The number after S is the encryption difficulty level


# Unlock file
To open the encryption, you must use the following command
RM.Unlock(The name of the encrypted file)
Before unlocking encryption, please put the encrypted file along with its key in the program folder -->
