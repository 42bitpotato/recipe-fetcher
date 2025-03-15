import requests
import os
import shutil

def main():

    def set_env():
        if os.listdir(path="test_env") != []:
            shutil.rmtree("test_env")
            os.mkdir("test_env")
        with open("html_file", "w") as new_html_page:
            new_html_page.write(new_html_string)

if __name__ == "__main__":
    main()