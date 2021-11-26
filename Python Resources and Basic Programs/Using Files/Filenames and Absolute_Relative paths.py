import os
#os.path.join allows the program to use the correct directory regardless of the operating system
print(os.path.join("folder1","folder2","file.png"))

#Gets the current directory, or the same folder in which this progam is in
print(os.getcwd())

#Changes the directory to wherever you set it to
os.chdir("c:\\")
print(os.getcwd())


#c:\\folder1\folder2\folder3\spam.png <- this is an absolute file path.
#spam.png <- is a relative file path, assumes it is wherever the root/current file path
# . and .. means this current folder or the parent one (. current / .. parent )

#checks to see if a path exists
print(os.path.exists("c:\\folder\\folder2\spam.png"))

