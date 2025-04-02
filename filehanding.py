file = open('Codingal.txt',)
print(file.read())
file.close()

file1 = open('Codingal.txt', 'w')
file1.write('File is in write mode')
file1.write('Welcome to the business docuement')
file.close()