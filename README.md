# File Organizer

A Python script that organizes files into folders based on file types and extensions.

## Features
- Sorts Images, Documents, Videos, Audio, and Others
  - Images (`.jpg`, `.png`, `.jpeg`, `.gif`, `.bmp`, `.svg`)
  - Documents (`.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.pptx`)
  - Videos (`.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`)
  - Audio (`.mp3`, `.wav`, `.flac`, `.aac`)
  - Others (any file not matching above categories)
- Handles duplicate filenames by adding suffixes (e.g. "file_1.txt")
- Creates logs with file sizes
- Undo option to restore files and delete unwanted empty folders

## How to Run

Clone the repository
```bash
   git clone https://github.com/<your-username>/file-organizer.git
   cd file-organizer
```

Run the script
```bash
python file_organizer.py
```

Enter path to your directory
```bash
Enter directory path: C:\Users\YourName\Downloads
```

Undo the organization: y if yes n if no
```bash
Undo organization? (y/n): y
```
