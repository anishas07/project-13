file = open('project.txt', 'r')
print(file.read())
file.close()

file2 = open('project.txt', 'w')
file2.write('File is in write mode\n')
file2.write('Welcome to the document about india\n')
file2.close()


file2 = open('project.txt', 'r')
print(file2.read())
file2.close()

file2 = open('project.txt', 'a')
file2.write('Appending  mode.\n')
file2.write('Add your resarch to the document.\n')
file2.close()
