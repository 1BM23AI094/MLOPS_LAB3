import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

def list_files(path):
    return os.listdir(path)

if __name__ == "__main__":
    create_directory("test_folder")
    print(list_files("."))