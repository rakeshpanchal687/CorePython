import shutil

source = "C:/Users/rakes/Downloads/converted.png";
target = "../file/Myimage.png";

shutil.copyfile(source, target)

print(source + " is copied to " + target)
