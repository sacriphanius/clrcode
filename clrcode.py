import fileinput

print("Which word do you want to replace? (custom_colors)")
old_word = input()

print("With which word do you want to replace it? (sample_color or original_color)")
new_word = input()

print("Enter the path and name of the file: ")
file_path = input()

# Replacing the specified word in the file
with fileinput.FileInput(file_path, inplace=True) as file:
    for line in file:
        print(line.replace(old_word, new_word), end='')

print("Replacement process completed.")
