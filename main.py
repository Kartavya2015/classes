new_file = open('index.html', 'x')
new_file.close

import os
print("processing...")
if os.path.exists("index.html"):
    os.remove("my.py")

else:
    print("sorry,check for\ndoes file exist?\nis the name correct?\nwe can create new!")

my_py = open("my_py", "w")
my_py.write("hi nice to meet you\n i am siri")
my_py.close()

os.remove('index.html')
os.rmdir('part 2')