import os

# Define folder name (change as needed)
folder_name = "labels"

# Create the folder if it doesn't exist
os.makedirs(folder_name, exist_ok=True)

class_id = 0
x_center = 0.5
y_center = 0.5
width = 0.3
height = 0.4

for i in range(91):  # creates files 0.txt through 90.txt
    file_path = os.path.join(folder_name, f"{i}.txt")
    with open(file_path, "w") as f:
        f.write(f"{class_id} {x_center} {y_center} {width} {height}")
