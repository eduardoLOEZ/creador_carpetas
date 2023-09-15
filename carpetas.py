import os

# ------ CREATE HTML ------
def create_html(folder_path):
    # Create an index.html file in the specified path
    with open(os.path.join(folder_path, "index.html"), "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Page</title>\n</head>\n<body>\n<h1>My Page</h1>\n</body>\n</html>")

# ------ CREATE CSS ------
def create_css(folder_path):
    # Create a styles.css file in the specified path
    with open(os.path.join(folder_path, "styles.css"), "w") as f:
        f.write("/* CSS styles here */")

# ------ CREATE JS ------
def create_js(folder_path):
    # Create a main.js file in the specified path
    with open(os.path.join(folder_path, "main.js"), "w") as f:
        f.write("// JavaScript code here")

# ------ MAIN FUNCTION ------
def create_dir(base_path):
    # Create 25 folders
    for i in range(1, 26):
        # Ask the user for the folder name
        folder_name = input(f"Enter the name for folder {i}: ")
        
        # Combine the base path with the folder name
        folder_path = os.path.join(base_path, folder_name)

        # If the folder doesn't exist, create it
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        else:
            print(f"The folder {folder_name} already exists.")

        # Add HTML, CSS, and JS files to each folder
        create_html(folder_path)
        create_css(folder_path)
        create_js(folder_path)

    # Success
    print("Folders created successfully. You can start your projects now.")

# MAIN
if __name__ == "__main__":
    base_path = "/Users/hp/Documents/first_midterm-pages"
    create_dir(base_path)
