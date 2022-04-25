import pandas as pd
import numpy as np
import os
import xlsxwriter
from datetime import datetime
from openpyxl import load_workbook
from datetime import datetime

#Select RAWLOGPATH from excel /remove
RAWLOGPATH = r'C:\Users\User\Desktop\proyecto satelite\Satelite'
TITLES = ['Hora en Float', 'Fecha y Hora de Inicio', 'Identificador Decimal', 'Largo del Paquete', 'Identificador','00','01','02','03','04','05','06','07','08','09','A','B','C','D','E','F','10','11','12','13','14','15','16','Concatenación de los paquetes']
FILENAME = "test"
OUTPUTPATH = r'C:\Users\User\Desktop\proyecto satelite\\' + FILENAME + '.xlsx'
X_DATEFL= 0
X_DATESTR = 1
#X_PACKAGESRECIVED = 2
#X_PACKAGESLOST = 3
#X_PACKAGESPORCENT = 4
X_IDENDECIMAL = 2
X_LENGHT = 3
X_IDEN = 4
X_HEXSTART = 5
X_CONCAT = 27

yLenght = 0
startIndex = 0

#We need this variables to check if the packages we are reciving are new due to the identificator repeating
chunkC = 0

def ReadNextFile(excelName):
	df = pd.read_excel(RAWLOGPATH + '\\' + excelName, index_col=None, na_values=['NA'])
	return df

def CreateExcel():

	#display the whole string
	pd.set_option('display.max_colwidth', None)


	#Initialize Writer
	writer = pd.ExcelWriter(FILENAME+".xlsx", engine="xlsxwriter")
	#Create empty dataframe
	df_empty = pd.DataFrame({'' : []})
	df_empty.empty
	#Create excel
	df_empty.to_excel(writer, startrow=0, startcol=0, index=False)
	worksheet = writer.sheets['Sheet1']

	#Write title
	for i in range(len(TITLES)):
		worksheet.write(0, i,TITLES[i])

	return writer, worksheet

def SaveDF(df, writer, worksheet):
	#Write excel
	writer.save()
	writer = pd.ExcelWriter(FILENAME + ".xlsx", engine="xlsxwriter")
	df.to_excel(writer,  index=False)
	worksheet = writer.sheets['Sheet1']
	#Write excel
	writer.save()

def SaveExcel(writer):
	#Write excel
	writer.save()
	#Select the RAWLOGPATH of the new excel (this helps due to the new format)
	print(OUTPUTPATH)
	df = pd.read_excel(OUTPUTPATH, index_col=None, na_values=['NA'])
	writer = pd.ExcelWriter(FILENAME + ".xlsx", engine="xlsxwriter")
	df.to_excel(writer,  index=False)
	worksheet = writer.sheets['Sheet1']
	return df, writer, worksheet

def WriteNewExcel(df, chunkC):
	#Loop all the rows
	#Create Chunks of data so there is no ovewrite
	for i in range(len(df.index)):
		if(i >= 4): #we start at 4, because the first row are trash data

			x_message = 4
			cur_row =df.iat[i,x_message]
			
			#get lenght
			split_df_lenght = cur_row.split("length\": ", 1)
			cur_lenght = split_df_lenght[1].split(",",1)[0]
	
			#get value
			split_df_value = cur_row.split("value\":",1)
			cur_value = split_df_value[1].split("\"",2)[1]
	
			#get identificador
			cur_identificador = cur_value[0:4]
			#get parte
			cur_parte = '0x'+cur_value[4:6]
			
			#calculate where to put the rest of the value
			parteDec = int(cur_parte, 16)
			idenDec = int(cur_identificador, 16)
		
			#get date	
			split_df_date = cur_row.split("unixTime\": ", 1)
			cur_datefl = int(split_df_date[1].split("\"",2)[1])
			cur_datestr = datetime.utcfromtimestamp(cur_datefl).strftime('%Y-%m-%d %H:%M:%S')
			
			lastIden = cur_identificador
			#Write first set of data and Update Ytrans
			yTrans= idenDec+3+chunkC
			#write length
			worksheet.write(yTrans, X_LENGHT, cur_lenght)
			#write identificador
			worksheet.write(yTrans, X_IDEN, cur_identificador)
			worksheet.write(yTrans, X_IDENDECIMAL, idenDec)
			#write value
			worksheet.write(yTrans, X_HEXSTART+parteDec, cur_value[6:])
			#write date
			worksheet.write(yTrans, X_DATESTR, cur_datestr)
			worksheet.write(yTrans, X_DATEFL, cur_datefl)

	return chunkC

def FillEmptyWithJ(df, startIndex):
	##fill J for empty cells
	print("fill 1")
	for y in (n+1 for n in range(len(df.index)-1 - startIndex)):
		cellsEmpties = 0
		print(y + startIndex)
		for x in range(23):
			#get length
			jAmount = df.iat[y+startIndex, X_LENGHT]
			jString = ""
			
			#If the length value is not null, add J
			if(np.isfinite(jAmount)):
				for j in range(int(jAmount)):
					jString += 'J';
			#Write the number of J to the cell if empty
			if(pd.isnull(df.iat[y+startIndex,x+X_HEXSTART])):
				worksheet.write(y+startIndex+1,x+X_HEXSTART,jString)
				cellsEmpties+=1

		#Write The amount of packages missed
		#if(pd.isnull(df.iat[y+startIndex,X_LENGHT])):#check if row is not empty
		#	continue
		#else:
		#	worksheet.write(y+startIndex+1,X_PACKAGESRECIVED,(23 -cellsEmpties))
		#	worksheet.write(y+startIndex+1,X_PACKAGESLOST,(cellsEmpties))
		#	worksheet.write(y+startIndex+1,X_PACKAGESPORCENT,((23-cellsEmpties)/23)*100)

def ConCatRow(df, startIndex):
	#Concat all the rows
	for y in (n+1 for n in range(len(df.index)-1 - startIndex)):
		fullMessage = ""
		print(y + startIndex)
		for x in range(23):		
			if(pd.isnull(df.iat[y+startIndex,x+X_HEXSTART])):
				continue
			else:
				curCell = df.iat[y+startIndex,x+X_HEXSTART]
				fullMessage += curCell	
		
			#check if message is shorter than 322
			if(len(fullMessage) < 322 and x == 22):
				dif = 322 - len(fullMessage)
				for i in range(dif):
					fullMessage += 'J'
			worksheet.write(y+startIndex+1,X_CONCAT+1,fullMessage)

def OrderDF(df):
	df = df.sort_values(by =['Hora en Float', 'Identificador Decimal'])
	return df
#------------------------------------------------------------
#Create a list of all files in folder
excelList = os.listdir(RAWLOGPATH)


#Create Excel
createData = CreateExcel()
writer = createData[0]
worksheet = createData[1]

for i in range(len(excelList)):
	#get new excel
	df = ReadNextFile(excelList[i])
	print("write")
	#Write New Excel
	saveData = WriteNewExcel(df, chunkC)
	chunkC = saveData
	print("Fill")
	#Save
	saveData = SaveExcel(writer)
	df = saveData[0]
	writer = saveData[1]
	worksheet = saveData[2]

	#Save Lenght of df, to write next file below the last one
	chunkC += len(df.index)

	FillEmptyWithJ(df, startIndex)

	#Save
	saveData = SaveExcel(writer)
	df = saveData[0]
	writer = saveData[1]
	worksheet = saveData[2]
	print("Concat")
	ConCatRow(df, startIndex)

	#Save
	saveData = SaveExcel(writer)
	df = saveData[0]
	writer = saveData[1]
	worksheet = saveData[2]

	startIndex =len(df.index)-1


	#Show progress
	print(str("{:.2f}".format(((i+1)/len(excelList)*100))) + '%'+' of files completed')


print(len(df.index))
saveData = OrderDF(df)
df = saveData

SaveDF(df, writer, worksheet)

