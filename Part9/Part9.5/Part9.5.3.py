text = input()
if 5 <= len(text) <= 15 and text[0] == "@":
    if (text.islower() and text[1:].isalnum()) or text[1:16].isdigit():
        print("Correct")
    else:
        print("Incorrect")
else:
    print("Incorrect")
