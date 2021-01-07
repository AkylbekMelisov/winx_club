def open_file(filename,text):
    file1 = open(filename,'w')
    file1.write(text)
open_file('test.txt','hellow!')
