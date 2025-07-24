

import os
print("processing...")
if os.path.exists("index.html"):
    os.remove("index.htm")
    new_file = open('index.htm', 'x')
    new_file.close()
else:
    print("sorry,check for:\ndoes file exist?\nis the name correct?\nwe can create new!")

py = open("my_py", "w")
py.write("hi nice to meet you\n i am siri")
py.close()

os.remove('index.html')
