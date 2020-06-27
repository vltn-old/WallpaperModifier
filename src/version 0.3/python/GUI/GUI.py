import time
import os
import sys
import ctypes
import random
import PIL
import eel



def GUI():
    width = 800;
    height = 450;

    eel.init('../../interface')
    eel.start('main.html')

    

"""def setBackgroundImage(window, width, height):
    file = open("../data.txt", "r");
    content = file.read();
    file.close();

    data = content.split(';');
    pathData = data[0].split(',');
    actualWallpaperData = data[1].split(',');

    imagePath = pathData[1] + "\\" + actualWallpaperData[1];

    image = ImageTk.PhotoImage(Image.open(imagePath).resize((width, height)));
    w = tk.Label(window, image=image);
    w.pack();"""



def checkIfWindows(autoMode = False):
    if os.name != "nt":
        if autoMode == False:
            errorNotWindows();

            time.sleep(2);
            return False;
        else:
            return False;



def checkIfDataFileExist():
    if os.path.isfile("../../data.txt") == False:
        return False;

def restoringDataFileProcess():
    print("\u001b[31mThe data file does not exist or have been deleted. Creating new one ! Your settings are reset to default make sure you restore your settings to use WallpaperModifier.\u001b[0m \n");
    
    print("\u001b[33mYou can create new file but your settings will be reset or import your data file to restore your settings.\u001b[0m");
    answer = input("\u001b[33mDo you want to create new data file ? Type YES if you want a new data file or type NO if you want to import your's.\u001b[0m [yes][no]: ");

    if answer == "yes" or answer == "y":
        newFileData = ["wallpaperPath, ;\n", "actualWallpaper, ;\n", "previousWallpaper, ;\n"];
        writeInFile([newFileData[0], newFileData[1], newFileData[2]]);

        print("\n\u001b[32mA new empty data file have been created.\u001b[0m \n");
    else:
        print("\nYou want to import your data file. You need to set the data file in the app directory.");
        print("\u001b[32mApplication directory: " + os.path.dirname(os.path.abspath(__file__)) + "\u001b[0m");
        print("\n\u001b[33mThe programm need to be restart to save and apply changes.\u001b[0m");

        bye();
        sys.exit(1);



def checkPathAlreadySet(autoMode = False):
    file = open("../../data.txt", "r");
    content = file.read();
    file.close();

    data = content.split(';');
    pathData = data[0].split(',');

    if pathData[1] != " ":
        return True;



def setPath(command):
    if checkPathAlreadySet() == True:
        answer = input("\u001b[33mThe path to your wallpaper folder as already been set. Are you sure you want to change it ?\u001b[0m [yes][no]: ");

        if answer == "yes" or answer == "y":
            path = input("\nWhat is the new path of your wallpaper folder? : ");
        else:
            return True;
    else:
        path = input("\nWhat is the path of your wallpaper folder? : ");

    file = open("../../data.txt", "r");
    content = file.read();
    file.close();

    data = content.split(';');
    pathData = data[0].split(',');

    if path[0] == '"':
        path = path.split(path)[1];

    writeInFile([pathData[0], ",", path, ";", data[1], ";", data[2], ";"]);
    print();



def changeWallpaper():
    file = open("../../data.txt", "r");
    content = file.read();
    file.close();

    data = content.split(';');
    pathData = data[0].split(',');

    if pathData[1] == " ":
        errorPathNotSet();
        return False;

    files = os.listdir(pathData[1]);
    
    wallpaperName = files[random.randint(0, len(files) - 1)];
    ctypes.windll.user32.SystemParametersInfoW(20, 0, pathData[1] + "\\" + wallpaperName, 0);

    actualWallpaperData = data[1].split(',');
    previousWallpaperData = data[2].split(',');

    previousWallpaperData[1] = actualWallpaperData[1];
    actualWallpaperData[1] = wallpaperName;

    writeInFile([data[0], ";", actualWallpaperData[0], ",", actualWallpaperData[1], ";", previousWallpaperData[0], ",", previousWallpaperData[1], ";"]);



def restoreWallpaper():
    file = open("../../data.txt", "r");
    content = file.read();
    file.close();

    data = content.split(';');
    pathData = data[0].split(',');

    if pathData[1] == " ":
        errorPathNotSet();
        return False;

    actualWallpaperData = data[1].split(',');
    previousWallpaperData = data[2].split(',');

    if previousWallpaperData[1] == " ":
        errorNoPreviousWallpaper();
        return False;

    actualWallpaperData[1] = previousWallpaperData[1];

    ctypes.windll.user32.SystemParametersInfoW(20, 0, pathData[1] + "\\" + previousWallpaperData[1], 0);

    writeInFile([data[0], ";", actualWallpaperData[0], ",", actualWallpaperData[1], ";", previousWallpaperData[0], ",", previousWallpaperData[1], ";"]);



def writeInFile(data):
    file = open('../../data.txt', 'w');

    for i in data:
        file.write(i);

    file.close();



def help():
    text = "Welcome in the wallpaper modifier documentation. \n\n List of functions: \n _ next: Change the wallpaper to the next based of your changing method. \n _ previous: Restore the previous wallpaper. Works with only the last one. \n _ setpath:  Allow you to set the folder path where your wallpaper are stored in your computer.";
    tkinter.messagebox.showinfo("Help", text);

def errorPathNotSet():
    tkinter.messagebox.showerror("Error", "You didn't set your wallpaper folder path. Wallpaper folder can't be found.");

def errorNoPreviousWallpaper():
    tkinter.messagebox.showerror("Error", "There is no previous wallpaper in your history. Use 'next' function multiple time before using 'prev'.");

def errorNotWindows():
    tkinter.messagebox.showerror("Error", "Your are not on Windows operating system. Unfortunately this programm does not support other operating system than Windows.");



def main():
    if checkIfWindows() == False:
        return False;

    if checkIfDataFileExist() == False:
        restoringDataFileProcess();

    if checkPathAlreadySet() != True:
        errorPathNotSet();

    window = GUI();

if __name__ == "__main__":
    main();