#  Manual rainbow table *(reading a word list)*
* + - . + - * + - . - + * - + - . 

Use: Python3, Spyder
	-> libs: json, hashlib, urlib

"A rainbow table is a precomputed table for caching the output of cryptographic hash functions, usually for cracking password hashes. Tables are usually used in recovering a key derivation function (or credit card numbers, etc.) up to a certain length consisting of a limited set of characters."

    (uwu) ~~ 


First of all, the algorithm started reading the wordlist (data.json), which you can find in this repository :D. After that, creates an dictionary with the "passwords" and with the hashlib generate the hashes. Then, we have a wordlist in fact.

When an hash is inputed in decrypt() function (not a nice name lol) it verified if this hash has an password at wordlist, returning an response. ...We've created an rainbow table!


## Hashlib...
 + - . + - * + - . - + * - + - . 

 -> creating hash:
 
def password_with_hash():
   dictionary = {}
   for i in list_password():
       print(i,hashlib.sha256(i.encode()).hexdigest())
       dictionary[hashlib.sha256(i.encode()).hexdigest()]=i
   return dictionary
 
 more about hashlib -> [hashlib — Secure hashes and message digests — Python 3.9.1rc1 documentation](https://docs.python.org/3/library/hashlib.html)

## About json.. 
* + - . + - * + - . - + * - + - . 

"JavaScript Object Notation is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value). It is a very common data format, with a diverse range of applications, such as serving as a replacement for XML in AJAX systems."

more about .json with python -> [Python Read JSON File – How to Load JSON from a File and ... (freecodecamp.org)](https://www.freecodecamp.org/news/python-read-json-file-how-to-load-json-from-a-file-and-parse-dumps/#:~:text=JSON%20is%20a%20file%20format%20used%20to%20represent,and%20use%20the%20data%20in%20our%20program%20directly.)


## Urblib

* + - . + - * + - . - + * - + - . 


 more about urblib -> [urllib — URL handling modules — Python 3.9.1rc1 documentation](https://docs.python.org/3/library/urllib.html)