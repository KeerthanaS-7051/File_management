import os
import shutil

file_types = {
    "images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    "documents": ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    "videos": ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    "audio": ['.mp3', '.wav', '.flac', '.aac']
}
other = "others"
log_file = "file_organizer.log"

#get file type from extension
def get_category(ext):
    for cat, exts in file_types.items():
        if ext.lower() in exts:
            return cat
    return other

#new names for duplicates
def get_unique_name(folder, filename):
    base, ext = os.path.splitext(filename)
    new_name = filename
    count = 1
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{base}_{count}{ext}"
        count += 1
    return new_name

def organize(directory):
    moved = []
    with open(log_file, "w", encoding="utf-8") as log:
        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            if os.path.isdir(path):     #skip folders
                continue
            try:
                ext = os.path.splitext(file)[1]
                cat = get_category(ext)
                folder = os.path.join(directory, cat)
                os.makedirs(folder, exist_ok=True)

                new_name = get_unique_name(folder, file)
                new_path = os.path.join(folder, new_name)

                shutil.move(path, new_path)
                moved.append((new_path, path))

                size = os.path.getsize(new_path)
                log.write(f"Moved {file} -> {folder}, Size: {size} bytes\n")
                print(f"    {file} moved to {folder}")

            except Exception as e:
                log.write(f"Error moving {file}: {e}\n")
                print(f"Could not move {file}: {e}")
    return moved

#undo organizing
def undo(moved):
    folders = set()
    for new, old in moved:
        try:
            shutil.move(new, old)
            folders.add(os.path.dirname(new))
            print(f"    Restored {os.path.basename(new)}")
        except Exception as e:
            print(f"Could not restore {new}: {e}")
    for f in folders:
        if os.path.isdir(f) and not os.listdir(f):
            os.rmdir(f)
            print(f"    Deleted {os.path.basename(f)}")

if __name__ == "__main__":
    directory = input("Enter directory path: ").strip()
    if not os.path.isdir(directory):
        print("Invalid path")
    else:
        moved_files = organize(directory)
        choice = input("Undo organization? (y/n): ").lower()
        if choice == 'y':
            undo(moved_files)
