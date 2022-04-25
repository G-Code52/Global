def createfile(path):
    File = open(path, 'w', encoding='utf-8')
    File.write("Title\t\t\t\tHexadecimal\t\t\t\tDecimal\n")

def saveText(path, string):
    File = open(path, 'a', encoding='utf-8')
    File.writelines(string)