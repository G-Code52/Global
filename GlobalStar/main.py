import decoding as dec
from text_writer import createfile
import pathRecognizer as pr
from filesRecognizer import obtainFiles
from saveExcell import CreateExcel
import os
                                    #PATH = r'D:\GlobalStar/test.xlsx'
PATHTEXT = '' #global variable of the .txt files paths
NAMETEXT = 1 #number of .txt
PATHCONCATEFILES = '' #global variable of the concate files paths
CONCATENAMESFILES = [] #global list for every concate file in the folder
NAME = 'Solo texto de concatenación' # name of the column
                        #NAME = 'Concatenación de los paquetes'
INDEX = 0

if __name__ == '__main__':
    PATHCONCATEFILES = pr.obtainPathConcateFiles()
    CONCATENAMESFILES = obtainFiles( PATHCONCATEFILES )
    print(CONCATENAMESFILES)

    for names in CONCATENAMESFILES:
        PATHTEXT = pr.obtainPathTxtResult(str(NAMETEXT)) #Obtain the path for the .txt results
        print(PATHTEXT)
        createfile(PATHTEXT) #Create a empty .txt file
        CreateExcel(NAMETEXT)

        path = os.path.join( PATHCONCATEFILES , names )
        print(path)

        df = dec.createDataframe( path )
        print(df)

        while True:
            data = dec.readData(df, NAME, INDEX)
            INDEX += 1
            if data != 0:
                lista_excell = dec.readString(data)
                createfile(lista_excell, INDEX)
            else:
                print("Final")
                break
        NAMETEXT += 1