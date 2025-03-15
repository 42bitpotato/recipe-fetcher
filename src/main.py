import os
import shutil
from download_content import *

def main():

    url = "https://www.koket.se/lax-med-sandefjordsas-och-citronfankal"

    if os.listdir(path="test_env") != []:
        shutil.rmtree("test_env")
        os.mkdir("test_env")

    dest_file_name = os.path.join("test_env", "html_file.html")
    html_data = get_html(url)

    with open(dest_file_name, "w") as html_file:
        html_file.write(html.prettify())

    print(html_file)

if __name__ == "__main__":
    main()