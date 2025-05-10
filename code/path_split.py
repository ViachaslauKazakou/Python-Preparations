import os
filename = "example.and.example.txt"
basename, extension = os.path.splitext(filename)
print(extension)