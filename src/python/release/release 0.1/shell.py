import pyfiglet
import time
import os
import ctypes
import random

def welcome():
    print(pyfiglet.Figlet(font = 'slant').renderText('     Wallpaper'));

    print("\nWelcome to Wallpaper modifier !");
    print("   Author: Valentin Le Lièvre \n   Version: 0.1 \n   License: MIT \n");

def bye():
    print("Thanks to use wallpaper modifier. Hope to see you soon ! \n");

    time.sleep(2);

def checkIfWindows():
    if os.name != "nt":
            print("\u001b[31m\nYour are not on Windows operating system. Unfortunately this programm does not support other operating system than Windows.\u001b[0m \n");
            return False;
    else:
        return True;

def getInput():
    command = input(">>> ");

    return command;

def excecuteCommand(command):
    if command == "setPath" or command == "setpath":
        setPath(command);
    elif command == "next":
        changeWallpaper();
    elif command == "help":
        help();
    elif command == "quit":
        return False;
    else:
        error(command);

def setPath(command):
    checkIfDataFileAlreadyExist();

    if checkPathAlreadySet() == True:
        print('fd');

    return True;

def checkIfDataFileAlreadyExist():
    if os.path.isfile("data.txt") == False:
        file = open("data.txt", "a+");
        file.close();

        print("\u001b[32mThe data file does not exist or have been deleted. Creating new one ! Your settings are be reset to default make sure you restore your settings.\u001b[0m \n");
    else:
        return True;

def checkPathAlreadySet():
    file = open("data.txt", "r");

    content = file.read();
    data = content.split(';');
    pathData = data[0].split(',');

    file.close();

    if pathData[1] != " ":
        answer = input("\u001b[33mThe path to your wallpaper folder as already been set. Are you sure you want to change it ?\u001b[0m [yes][no]: ");

        if answer == "yes" or answer == "y":
            path = input("\nWhat is the new path of your wallpaper folder? : ");
        else:
            return True;
    else:
        path = input("\nWhat is the path of your wallpaper folder? : ");

    if path[0] == '"':
        path = path.split(path)[1];

    writeInFile([pathData[0], ",", path, ";"]);

    print();
    return True;

def writeInFile(data):
    file = open('data.txt', 'w');

    for i in data:
        file.write(i);

    file.close();

def changeWallpaper():
    file = open("data.txt", "r");

    content = file.read();
    data = content.split(';');
    pathData = data[0].split(',');
    path = pathData[1];

    file.close();

    files = os.listdir(path);
    
    wallpaperName = files[random.randint(0, len(files) - 1)];
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "\\" + wallpaperName, 0);

def help():
    text = ["Welcome in the wallpaper modifier documentation. Type help --function name for more infos about a specific function.", "", "How to use:", " _ <function name> [arguments] --optinal arguments", "", "List of functions:", " _ test [number to print]", " _ quit", ""];

    for i in text:
        print(i);

def error(command):
    print("\u001b[31mThe function: " + command + " does not exist ! Try to correct the function or use 'help' for more information about the avaible functions.\u001b[0m \n");

def main():
    welcome();

    if checkIfWindows() == False:
        return True;

    print("Type help to see command options.");
    while True:
        command = getInput();
        returnedValue = excecuteCommand(command);

        if returnedValue == False:
            bye();
            break


    """for i in range(50):
        print("\u001b[" + str(i) + "mHi, coders. This is pink output.\u001b[0m", " " + str(i));"""


if __name__ == "__main__":
    main();