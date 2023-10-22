import urllib.request
import zipfile
import os
import shutil

url = "https://github.com/neebooo/pySBGUI/archive/refs/heads/main.zip"

zip_path, _ = urllib.request.urlretrieve(url)
with zipfile.ZipFile(zip_path, "r") as f:
    for finfo in f.namelist():
        if (
            finfo.startswith("pySBGUI-main/static")
            or finfo.startswith("pySBGUI-main/templates")
            or finfo.startswith("pySBGUI-main/pygui.py")
        ):
            f.extract(finfo, ".")
# After done move everything from pySBGUI-main to the root directory
source_directory = "pySBGUI-main"
contents = os.listdir(source_directory)

# Move each item from the 'pySBGUI-main' folder to the current working directory
for item in contents:
    source_path = os.path.join(source_directory, item)
    destination_path = os.path.join(
        os.getcwd(), item
    )  # Use os.getcwd() to get the current working directory
    shutil.move(source_path, destination_path)
shutil.rmtree(source_directory)
