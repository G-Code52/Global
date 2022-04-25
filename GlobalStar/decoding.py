import pandas as pd
from text_writer import saveText
import saveExcell as se




DICTIONARY = [
    ['Start=', 8],

    ['PowAmpTemp=', 4],
    ['LastRSSI=', 4],
    ['GndRSSI=', 4],

    ['PowConvVolt1=', 4],
    ['PowConvVolt2=', 4],
    ['PowConvVolt3=', 4],
    ['BattVolt=', 4],
    ['CurrIn1=', 4],
    ['CurrIn2=', 4],
    ['CurrIn3=', 4],
    ['BoostConvCurr=', 4],
    ['BattOutCurr=', 4],
    ['OutCurr1=', 4],
    ['OutCurr2=', 4],
    ['OutCurr3=', 4],
    ['OutCurr4=', 4],
    ['OutChanStat1=', 2],
    ['OutChanStat2=', 2],
    ['OutChanStat3=', 2],
    ['OutChanStat4=', 2],
    ['I2cWdtTimeLeft=', 8],
    ['GndWdtTimeLeft=', 8],
    ['WdtGndRebootNum=', 8],
    ['BattTempSen=', 4],

    ['SenAvalue=', 4],
    ['PwmCurr=', 4],
    ['LastObcRebootCause=', 8],
    ['MagX=', 8],
    ['MagY=', 8],
    ['MagZ=', 8],
    ['GyroX=', 8],
    ['GyroY=', 8],
    ['GyroZ=', 8],

    ['CoarSunSenValPosY=', 4],
    ['CoarSunSenValPosX=', 4],
    ['CoarSunSenValNegX=', 4],
    ['CoarSunSenValNegY=', 4],
    ['CoarSunSenValNegZ=', 4],
    ['SolPanTempPosY=', 8],
    ['SolPanTempPosX=', 8],
    ['SolPanTempNegX=', 8],
    ['SolPanTempNegY=', 8],
    ['SolPanTempNegZ=', 8],
    ['BdotStat=', 2],
    ['BdotValLowPass1=', 8],
    ['BdotValLowPass2=', 8],
    ['ValDetumState=', 2],

    ['RfChan=', 2],
    ['BurstsNum=', 2],
    ['MinBurInt=', 2],
    ['MaxBurInt=', 2],
    ['HardStat=', 2],
    ['SecSinLastTran=', 4],
    ['SecUntNextTran=', 4],
    ['PkgSizeLastCurrMsg=', 2],
    ['CurrWaitSendBurNum=', 2],
    ['SecUntBurTranNum2=', 4],
    ['SecUntBurTranNum3=', 4],
    ['TotMsgTranCurrMode=', 4],
    ['TotPkgTranCountSinPowOn=', 4],
    ['AntTemp=', 2],
    ['SpiSenTemp=', 4],
    ['UnixTime=', 8],
    ['End=', 10]
]

PATH = r'C:\Users\Mauricio\Desktop\Global\GlobalStar\prueba.txt'
cont = 1
lista = []

def createDataframe(path):
    df = pd.read_excel(path)
    return df

def readData(df, name, row): #read excell and make a dataframe
    try:
        #print(row)
        data = df.at[row, name]
        a = pd.isnull(data)

        if a:
            print("vacio")
            return 0

        saveText(PATH, "\n[" + str(row) + "]\n")

        return data
    except:
        print("Something went wrong")
        return 0


def readString(string):#give the string an read the dictionary
    control = 0

    for v in DICTIONARY:
        stringText = v[0]

        readSubString(control, control + v[1], string, stringText)
        control += v[1]

def readSubString(ini, end, string, stringText): #read the part of the dictionary and check if is a "J" part
    subString = string[ini]

    for n in range(ini + 1, end):
        subString += string[n]

    #stringText += subString
    print(stringText)

    if 'J' in subString:
        stringText += ' \n'
        DataList(stringText)
        saveText(PATH, stringText)
        return

    convert(subString, stringText)


def convert(hexa, stringText): #convert de part hexadecimal to decimal
    dec = int(hexa, 16)
    DataList(dec)

    stringText += str(dec) + '\n'

    print(stringText)
    saveText(PATH, stringText)
    return

def DataList(dec):
    global cont
    global lista
    if (cont <= 65):
        lista.append(dec)
        cont += 1
    else:
        se.createFile(lista)
        del lista[1 : 65]
