import os

path = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Copy.txt'
dir = 'C:\\Users\\dell\\OneDrive\\Desktop\\Coding challenges\\FIle_Handling\\Empty_folder'
try:
    os.remove(path)
    os.rmdir(dir)

except PermissionError:
    print("You do not have permission to delete this!")
except FileNotFoundError:
    print("FIle was not file")

else:
    print('File/Directory was deleted successfully')