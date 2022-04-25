import decoding as dec
from text_writer import createfile
from pathRecognizer import obtainPath
import saveExcell as se

PATH = r'C:\Users\Mauricio\Desktop\Global\GlobalStar\AZT_ORR_MS_CCTN_2.xlsx'
#PATH = r'D:\GlobalStar/test.xlsx'
PATHTEXT = r'C:\Users\Mauricio\Desktop\Global\GlobalStar\prueba.txt'
NAME = 'Solo texto de concatenación'
#NAME = 'Concatenación de los paquetes'
INDEX = 0

if __name__ == '__main__':
    obtainPath()
    createfile(PATHTEXT)
    df = dec.createDataframe(PATH)

    while True:
        for v in range(0, 10):
            data = dec.readData(df, NAME, INDEX)
            INDEX += 1
            if data != 0:
                dec.readString(data)
            else:
                print("Final")
                break
        se.createFile(r'C:\Users\Mauricio\Desktop\Global\GlobalStar\RawResultsTXT')
