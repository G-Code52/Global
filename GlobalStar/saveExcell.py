import pandas as pd
import numpy as np
import os
from pathRecognizer import obtainPathExcellResult

writer = 0
worksheet = 0

def createFile(lista, row):
    HK = "Final"
    df = pd.DataFrame(lista, columns = [HK + row])


def CreateExcel(NUM):

	#display the whole string
	pd.set_option('display.max_colwidth', None)


	#Initialize Writer
	global writer
	writer = pd.ExcelWriter(os.path.join(obtainPathExcellResult(), "Final"+ NUM + ".xlsx"), engine="xlsxwriter")
	#Create empty dataframe
	df_empty = pd.DataFrame({'' : []})
	df_empty.empty
	#Create excel
	df_empty.to_excel(writer, startrow=0, startcol=0, index=False)
	global worksheet
	worksheet = writer.sheets['Sheet1']

	return writer, worksheet