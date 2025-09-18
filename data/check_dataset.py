import os
from glob import glob

# Path to your dataset
data_dir = r"D:\projects\mini_project\data"

# Define train and validation paths
train_dir = os.path.join(data_dir, "train")
val_dir = os.path.join(data_dir, "val")

# Function to check dataset
def check_dataset(path, set_name):
    print(f"\nChecking {set_name} dataset in: {path}")
    classes = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print(f" Found classes: {classes}")

    for cls in classes:
        img_files = glob(os.path.join(path, cls, "*"))
        print(f"  -> {cls}: {len(img_files)} images")

# Run checks
check_dataset(train_dir, "Train")
check_dataset(val_dir, "Validation")
