import os 
import wget 
import zipfile
import shutil

def main():
    try:
        os.mkdir("data")
    except FileExistsError: 
        print("delet")
        shutil.rmtree('data')
        os.mkdir("data")

    os.chdir("data")
    url = "https://donnees.roulez-eco.fr/opendata/instantane"

    file = wget.download(url)


    shutil.unpack_archive(file, "./")

    os.chdir("../")
