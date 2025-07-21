file_read = open('index.html', 'r')
print(file_read.read)
file_read.close

file_write = open('index.html', 'w')
print(file_write.write)
file_write.close