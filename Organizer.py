import os
import shutil

# ---
# 1. Welcome the user and get the source path.
# ---
print("Welcome to the self-organizer!")
print("This script will sort files into subdirectories based on their type.")

sourcepath = str(input("Enter the path which you want to organize: "))

# ---
# 2. Handle potential errors with the source path.
#    This is a major improvement for robustness.
# ---
if not os.path.exists(sourcepath):
    print(f"Error: The path '{sourcepath}' does not exist.")
    exit() # Exit the script if the path is invalid.
elif not os.path.isdir(sourcepath):
    print(f"Error: The path '{sourcepath}' is not a directory.")
    exit()

# ---
# 3. Use a dictionary to map file extensions to destination folder names.
#    This makes the code much cleaner and easier to expand.
# ---
# Get user input for destination paths with defaults
desti_paths = {
    'images': str(input("Enter directory for Raster Images (default: 'Images'): ")) or "Images",
    'vector_images': str(input("Enter directory for Vector Images (default: 'Vector Images'): ")) or "Vector Images",
    'music_video': str(input("Enter directory for Music & Videos (default: 'Music & Videos'): ")) or "Music & Videos",
    'documents': str(input("Enter directory for Documents, Spreadsheets, & Presentations (default: 'Documents'): ")) or "Documents",
    'programming_files': str(input("Enter directory for Programming Files (default: 'Programming Files'): ")) or "Programming Files",
    'others': str(input("Enter directory for Other files (default: 'Others'): ")) or "Others"
}

# ---
# 4. Define a comprehensive mapping of extensions to their category.
#    Using lowercase extensions ensures case-insensitivity.
# ---
extension_map = {
    # Raster Images (Existing)
    '.png': desti_paths['images'], '.jpg': desti_paths['images'], '.gif': desti_paths['images'], '.jpeg': desti_paths['images'],
    '.webp': desti_paths['images'], '.bmp': desti_paths['images'], '.tiff': desti_paths['images'], '.tif': desti_paths['images'],

    # Vector Images (New Category)
    '.svg': desti_paths['vector_images'], '.ai': desti_paths['vector_images'], '.psd': desti_paths['vector_images'],
    '.eps': desti_paths['vector_images'], '.indd': desti_paths['vector_images'],

    # Music/Video (Existing + added .mp3, .wav, .m4a for common audio)
    '.mp4': desti_paths['music_video'], '.mpg': desti_paths['music_video'], '.mpeg': desti_paths['music_video'], '.swf': desti_paths['music_video'],
    '.vob': desti_paths['music_video'], '.wmv': desti_paths['music_video'], '.3g2': desti_paths['music_video'], '.3gp': desti_paths['music_video'],
    '.asf': desti_paths['music_video'], '.asx': desti_paths['music_video'], '.avi': desti_paths['music_video'], '.flv': desti_paths['music_video'],
    '.m2ts': desti_paths['music_video'], '.mkv': desti_paths['music_video'], '.mov': desti_paths['music_video'], '.mp3': desti_paths['music_video'],
    '.wav': desti_paths['music_video'], '.m4a': desti_paths['music_video'], '.ogg': desti_paths['music_video'], '.flac': desti_paths['music_video'],

    # Documents, Spreadsheets, & Presentations (Expanded Category)
    '.doc': desti_paths['documents'], '.docx': desti_paths['documents'], '.html': desti_paths['documents'], '.odt': desti_paths['documents'],
    '.pdf': desti_paths['documents'], '.txt': desti_paths['documents'], '.rtf': desti_paths['documents'],
    '.xls': desti_paths['documents'], '.xlsx': desti_paths['documents'], '.ods': desti_paths['documents'], # Spreadsheets
    '.ppt': desti_paths['documents'], '.pptx': desti_paths['documents'], '.key': desti_paths['documents'], # Presentations
    '.fig': desti_paths['documents'], # Figma files
    '.csv': desti_paths['documents'], '.md': desti_paths['documents'], # Common text-based docs

    # Programming Files (New Category)
    '.htm': desti_paths['programming_files'], '.py': desti_paths['programming_files'], '.java': desti_paths['programming_files'],
    '.js': desti_paths['programming_files'], '.exe': desti_paths['programming_files'], '.app': desti_paths['programming_files'],
    '.bin': desti_paths['programming_files'], '.c': desti_paths['programming_files'], '.cpp': desti_paths['programming_files'],
    '.h': desti_paths['programming_files'], '.sh': desti_paths['programming_files'], '.css': desti_paths['programming_files'],
    '.json': desti_paths['programming_files'], '.xml': desti_paths['programming_files'], '.yml': desti_paths['programming_files'],
    '.yaml': desti_paths['programming_files'], '.php': desti_paths['programming_files'], '.rb': desti_paths['programming_files'],
    '.go': desti_paths['programming_files'], '.swift': desti_paths['programming_files'], '.kt': desti_paths['programming_files'],
    '.ts': desti_paths['programming_files'], # TypeScript
    '.jsx': desti_paths['programming_files'], '.tsx': desti_paths['programming_files'], # React files
    '.dll': desti_paths['programming_files'], '.jar': desti_paths['programming_files'], # Executables/Libraries
}

# ---
# 5. Create the destination directories once, outside the loop.
#    This is more efficient and avoids repetitive checks.
# ---
print("\nCreating destination directories if they don't exist...")
# Use a set to ensure unique folder names are processed only once
for folder_name in set(desti_paths.values()):
    dest_path = os.path.join(sourcepath, folder_name)
    if not os.path.exists(dest_path):
        try:
            os.mkdir(dest_path)
            print(f"Created directory: '{folder_name}'")
        except OSError as e:
            print(f"Error creating directory '{folder_name}': {e}")
            # Decide if you want to exit or continue if a folder can't be created
            # For now, we'll just print the error and continue.

print("\nStarting to organize files...")

# ---
# 6. Iterate through the files and folders in the source directory.
# ---
sourcefiles = os.listdir(sourcepath)
for file_name in sourcefiles:
    # Build the full path to the file
    source_file_path = os.path.join(sourcepath, file_name)

    # ---
    # 7. Check if the item is a file, not a directory.
    #    This prevents errors when a folder exists in the source directory.
    # ---
    if os.path.isdir(source_file_path):
        # Skip the newly created destination directories themselves
        if file_name in desti_paths.values():
            print(f"Skipping destination directory: '{file_name}'")
        else:
            print(f"Skipping sub-directory: '{file_name}'")
        continue

    # Get the file extension and convert it to lowercase for robust matching
    _, file_extension = os.path.splitext(file_name)
    file_extension = file_extension.lower()

    # ---
    # 8. Use the dictionary to find the destination path.
    #    This replaces the long `if/elif` chain.
    # ---
    destination_folder = extension_map.get(file_extension, desti_paths['others'])
    # .get() is safer than direct access, provides a default if key not found

    destination_path = os.path.join(sourcepath, destination_folder, file_name)

    # ---
    # 9. Move the file and provide user feedback.
    #    Add a try-except block for moving files to handle permissions or other errors.
    # ---
    try:
        # Prevent moving a file onto itself if it's already in the correct folder
        if source_file_path != destination_path:
            shutil.move(source_file_path, destination_path)
            print(f"Moved: '{file_name}' -> '{destination_folder}/'")
        else:
            print(f"Skipped: '{file_name}' is already in its destination.")
    except shutil.Error as e:
        print(f"Could not move '{file_name}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred while moving '{file_name}': {e}")

print("\nOrganization complete!")
