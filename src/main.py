import os
import shutil
from copy_html import *

def main():

    url = "https://www.recepten.se/recept/koettfaerslimpa.html"

    if os.listdir(path="test_env") != []:
        shutil.rmtree("test_env")
        os.mkdir("test_env")

    dest_file_name = os.path.join("test_env", "html_file.html")

    with open(dest_file_name, "w") as html_file:
        html_file.write(get_html(url))

    print(html_file)

if __name__ == "__main__":
    main()