import os
import re


def main():
    # Strips junk from beat saber custom level folders

    # Replace this with the parent directory for where your beatsaber custom track folders are
    basedir = 'D:\\SteamLibrary\\steamapps\\common\\Beat Saber\\Beat Saber_Data\\CustomLevels'
    # basedir = 'A:\\Code_Dev\\My Utilities\\test'

    if not os.path.exists(basedir):
        print("Dir does not exist: " + basedir)
        exit(-1)

    print("Renaming folders in: " + basedir)
    for folder in os.listdir(basedir):
        if not os.path.isdir(os.path.join(basedir, folder)):
            print(os.path.join(basedir, folder) + " is not a directory")
            continue
        print(re.split("\(", folder))
        namesplit = re.split("\(", folder)
        if len(namesplit) > 1:
            print("namesplit[1] == " + namesplit[1])
            os.rename(os.path.join(basedir, folder), os.path.join(basedir, namesplit[1].strip(")")))


if __name__ == "__main__":
    main()
