import os
import random
import shutil

# Set your paths
src_images = "beetroot_images/"
src_labels = "labels/"
dst_root = "dataset/"

# Create destination folders
os.makedirs(os.path.join(dst_root, "images/train"), exist_ok=True)
os.makedirs(os.path.join(dst_root, "images/val"), exist_ok=True)
os.makedirs(os.path.join(dst_root, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(dst_root, "labels/val"), exist_ok=True)

# List all image files (assuming .jpg)
image_files = [f for f in os.listdir(src_images) if f.endswith('.jpg')]
random.shuffle(image_files)

# Split ratio (adjust if needed)
split = int(0.8 * len(image_files))
train_files = image_files[:split]
val_files = image_files[split:]

# Move images and labels
for f in train_files:
    shutil.move(os.path.join(src_images, f), os.path.join(dst_root, "images/train", f))
    shutil.move(os.path.join(src_labels, f.replace('.jpg', '.txt')), os.path.join(dst_root, "labels/train", f.replace('.jpg', '.txt')))

for f in val_files:
    shutil.move(os.path.join(src_images, f), os.path.join(dst_root, "images/val", f))
    shutil.move(os.path.join(src_labels, f.replace('.jpg', '.txt')), os.path.join(dst_root, "labels/val", f.replace('.jpg', '.txt')))
