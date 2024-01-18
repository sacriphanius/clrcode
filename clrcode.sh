#!/bin/bash

echo "Which word do you want to replace? (custom_colors)"
read old_word

echo "With which word do you want to replace it? (sample_color or original_color)"
read new_word

echo "Enter the path and name of the file: "
read file_path

# Replacing the specified word in the file
sed -i "s/$old_word/$new_word/g" "$file_path"

echo "Replacement process completed."
