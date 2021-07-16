from datetime import date, datetime
from zipfile import ZipFile
import os

class FileController:
    def CreateBackup(self):
        currentdate = date.today().strftime("%d-%m-%Y")
        currenttime = datetime.now().strftime("%H;%M;%S")
        backupname = f'Backup_{currentdate}_{currenttime}'
        zipObj = ZipFile(f'{backupname}.zip', 'w')
        
        # Add multiple files to the zip
        zipObj.write('logs.csv')
        zipObj.write('CDMS-data.db')

        print(f"{zipObj.filename} was created in directory '{os.getcwd()}'")
        # close the Zip File
        zipObj.close()