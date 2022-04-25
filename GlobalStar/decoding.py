import pandas as pd
from text_writer import saveText
import saveExcell as se

DICTIONARY = [
    ['Start=', 8, 1],

    ['PowAmpTemp=', 4, -1],
    ['LastRSSI=', 4, -1],
    ['GndRSSI=', 4, -1],

    ['PowConvVolt1=', 4, 1],
    ['PowConvVolt2=', 4, 1],
    ['PowConvVolt3=', 4, 1],
    ['BattVolt=', 4, 1],
    ['CurrIn1=', 4, 1],
    ['CurrIn2=', 4, 1],
    ['CurrIn3=', 4, 1],
    ['BoostConvCurr=', 4, 1],
    ['BattOutCurr=', 4, 1],
    ['OutCurr1=', 4, 1],
    ['OutCurr2=', 4, 1],
    ['OutCurr3=', 4, 1],
    ['OutCurr4=', 4, 1],

    ['OutChanStat1=', 2, 1],
    ['OutChanStat2=', 2, 1],
    ['OutChanStat3=', 2, 1],
    ['OutChanStat4=', 2, 1],
    ['I2cWdtTimeLeft=', 8, 1],
    ['GndWdtTimeLeft=', 8, 1],
    ['WdtGndRebootNum=', 8, 1],
    ['BattTempSen=', 4, -1],

    ['SenAvalue=', 4, -1],
    ['PwmCurr=', 4, 1],
    ['LastObcRebootCause=', 8, 1],
    ['MagX=', 8, -1],
    ['MagY=', 8, -1],
    ['MagZ=', 8, -1],
    ['GyroX=', 8, -1],
    ['GyroY=', 8, -1],
    ['GyroZ=', 8, -1],

    ['CoarSunSenValPosY=', 4, 1],
    ['CoarSunSenValPosX=', 4, 1],
    ['CoarSunSenValNegX=', 4, 1],
    ['CoarSunSenValNegY=', 4, 1],
    ['CoarSunSenValNegZ=', 4, 1],
    ['SolPanTempPosY=', 8, -1],
    ['SolPanTempPosX=', 8, -1],
    ['SolPanTempNegX=', 8, -1],
    ['SolPanTempNegY=', 8, -1],
    ['SolPanTempNegZ=', 8, -1],
    ['BdotStat=', 2,-1],
    ['BdotValLowPass1=', 8,-1],
    ['BdotValLowPass2=', 8,-1],
    ['ValDetumState=', 2,1],

    ['RfChan=', 2, 1],
    ['BurstsNum=', 2, 1],
    ['MinBurInt=', 2, 1],
    ['MaxBurInt=', 2, 1],
    ['HardStat=', 2,1],
    ['SecSinLastTran=', 4,1],
    ['SecUntNextTran=', 4,1],
    ['PkgSizeLastCurrMsg=', 2,1],
    ['CurrWaitSendBurNum=', 2,1],
    ['SecUntBurTranNum2=', 4,1],
    ['SecUntBurTranNum3=', 4,1],
    ['TotMsgTranCurrMode=', 4,1],
    ['TotPkgTranCountSinPowOn=', 4,1],
    ['AntTemp=', 2, 1], #char
    ['SpiSenTemp=', 4, 1],
    ['UnixTime=', 8, 1],
    ['End=', 10, 1]
]
lista = []
cont = 1
PATH = r'D:\GlobalStar\prueba.txt'

def createDataframe(path):
    df = pd.read_excel(path)
    return df

def readData(df, name, row): #read excell and make a dataframe
    try:
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
        #print(v[2])
        negativo = v[2]

        readSubString(control, control + v[1], string, stringText, negativo)
        control += v[1]
    return lista

def readSubString(ini, end, string, stringText, neg): #read the part of the dictionary and check if is a "J" part
    subString = string[ini]

    for n in range(ini + 1, end):
        subString += string[n]

    #stringText += "--" + subString + "--"  # debugger

    if 'J' in subString:
        stringText += '\n'
        DataList("-")
        saveText(PATH, stringText)
        return

    convert(subString, stringText, neg)


def convert(hexa, stringText, neg): #convert de part hexadecimal to decimal
    auxNeg = 0

    if neg == -1 and hexa[0] == "1":
        auxString = list(hexa)
        auxString[0] = '0'
        hexa = "".join(auxString)
        auxNeg = 1

    dec = int(hexa, 16)
    if auxNeg == 1:
        dec *= -1


    stringText += str(dec) + '\n'
    DataList(stringText)
    print(stringText)
    #print(stringText, end='')
    saveText(PATH, stringText)
    return

def DataList(dec):
    global cont
    global lista
    if (cont <= 65):
        lista.append(dec)
        cont += 1
        if (cont == 65):
            se.createFile(lista)
            lista.clear()
