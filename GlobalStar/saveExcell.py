import os
import shutil as sh
from pathRecognizer import obtainPath
import xlsxwriter as writer

x = True
workbook = writer.Workbook('FinalResult.xlsx')
worksheet = workbook.add_worksheet()

def createFile(lista):        #path: path where .xlsx saves
    cell_format = workbook.add_format({'bold': True, 'italic': True})
    if x == True:
        Plantilla(worksheet, cell_format)









def Plantilla(worksheet, cell_format):

    worksheet.write(1, 0, "Start", cell_format)
    worksheet.write(2, 0, "Power amplifier temperature [tenth of °C]", cell_format)
    worksheet.write(3, 0, "Last RSSI", cell_format)
    worksheet.write(4, 0, "GND RSSI", cell_format)
    worksheet.write(5, 0, "Power convertes voltage [mV] [PV1]", cell_format)
    worksheet.write(6, 0, "Power convertes voltage [mV] [PV2]", cell_format)
    worksheet.write(7, 0, "Power convertes voltage [mV] [PV3]", cell_format)
    worksheet.write(8, 0, "Battery voltage [mV]", cell_format)
    worksheet.write(9, 0, "Current in [mA] [1]", cell_format)
    worksheet.write(10, 0, "Current in [mA] [2]", cell_format)
    worksheet.write(11, 0, "Current in [mA] [3]", cell_format)
    worksheet.write(12, 0, "Boost converters current [mA]", cell_format)
    worksheet.write(13, 0, "Boost converters current [mA]", cell_format)
    worksheet.write(14, 0, "Output current [mA] [1]", cell_format)
    worksheet.write(15, 0, "Output current [mA] [2]", cell_format)
    worksheet.write(16, 0, "Output current [mA] [3]", cell_format)
    worksheet.write(17, 0, "Output current [mA] [4]", cell_format)
    worksheet.write(18, 0, "Output channels status [0 or 1] [1]", cell_format)
    worksheet.write(19, 0, "Output channels status [0 or 1] [2]", cell_format)
    worksheet.write(20, 0, "Output channels status [0 or 1] [3]", cell_format)
    worksheet.write(21, 0, "Output channels status [0 or 1] [4]", cell_format)
    worksheet.write(22, 0,  "I2C wdt time left [s]", cell_format)
    worksheet.write(23, 0, "GND wdt time left [s]", cell_format)
    worksheet.write(24, 0, "WDT GND reboot number", cell_format)
    worksheet.write(25, 0, "Batteries temperature sensor", cell_format)
    worksheet.write(26, 0, "Sensor A value", cell_format)
    worksheet.write(27, 0, "PWM current", cell_format)
    worksheet.write(28, 0, "Last OBC reboot cause", cell_format)
    worksheet.write(29, 0, "Magnetometer - X axis", cell_format)
    worksheet.write(30, 0, "Magnetometer - Y axis", cell_format)
    worksheet.write(31, 0, "Magnetometer - Z axis", cell_format)
    worksheet.write(32, 0, "Gyro - X axis", cell_format)
    worksheet.write(33, 0, "Gyro - Y axis", cell_format)
    worksheet.write(34, 0, "Gyro - Z axis", cell_format)
    worksheet.write(35, 0, "Coarse Sun Sensors Value +Y", cell_format)
    worksheet.write(36, 0, "Coarse Sun Sensors Value +X", cell_format)
    worksheet.write(37, 0, "Coarse Sun Sensors Value -X", cell_format)
    worksheet.write(38, 0, "Coarse Sun Sensors Value -Y", cell_format)
    worksheet.write(39, 0, "Coarse Sun Sensors Value -Z", cell_format)
    worksheet.write(40, 0, "Solar Panel's Temperature +Y", cell_format)
    worksheet.write(41, 0, "Solar Panel's Temperature +X", cell_format)
    worksheet.write(42, 0, "Solar Panel's Temperature -X", cell_format)
    worksheet.write(43, 0, "Solar Panel's Temperature -Y", cell_format)
    worksheet.write(44, 0, "Solar Panel's Temperature -Z", cell_format)
    worksheet.write(45, 0, "Bdot Status", cell_format)
    worksheet.write(46, 0, "Bdot Value from low-pass filter slow", cell_format)
    worksheet.write(47, 0, "Bdot Value from low-pass filter slow2", cell_format)
    worksheet.write(48, 0, "Value of detumbled state", cell_format)
    worksheet.write(49, 0, "RF Channel", cell_format)
    worksheet.write(50, 0, "# Bursts", cell_format)
    worksheet.write(51, 0, "Minimum Burst Interval", cell_format)
    worksheet.write(52, 0, "Maximum Burst Interval", cell_format)
    worksheet.write(53, 0, "Hardware Status", cell_format)
    worksheet.write(54, 0, "Number of Seconds since las transmission", cell_format)
    worksheet.write(55, 0, "Number of seconds until next transmission", cell_format)
    worksheet.write(56, 0, "Packet size of last or current message", cell_format)
    worksheet.write(57, 0, "Currently waiting on or sending burst number", cell_format)
    worksheet.write(58, 0, "Number of seconds until burst transmission number 2", cell_format)
    worksheet.write(59, 0, "Number of seconds until burst transmission number 3", cell_format)
    worksheet.write(60, 0, "Total messages transmitted in current mode", cell_format)
    worksheet.write(61, 0, "Total packet transmission count since hard power on", cell_format)
    worksheet.write(62, 0, "Antenna Temperature", cell_format)
    worksheet.write(63, 0, "Temperature of the SPI Sensor", cell_format)
    worksheet.write(64, 0, "Unix Time", cell_format)
    worksheet.write(65, 0, "END", cell_format)
    x = False
    return x






