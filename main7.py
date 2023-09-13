"""

Saving file content

"""


target_file = open(r"c:\Users\veri\Desktop\targetedfile.txt")

target_file_content = target_file.read()
target_file.close()

print(target_file_content)


"""

Replacing saved content

"""


what_char_input = input("What characters you want to replace?: ")

while True:
    if what_char_input not in target_file_content:
        print("Word not found!")
        what_char_input = input("What word you want to replace?: ")
    else:
        break

with_what_input = input("With what characters you want to replace it?: ")


while True:
    result = target_file_content.replace(what_char_input, with_what_input)
    print(result)
    break

input("Press any key to exit...")