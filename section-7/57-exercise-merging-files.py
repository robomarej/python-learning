import glob
import datetime

sampleFilesPath="57-sample-files"
fileNameList=glob.glob1(sampleFilesPath,"**")

def read_file(fileName):
    with open(fileName, "r") as file:
        return file.read()

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", "a") as file:
    for fileName in fileNameList:
        file.write(read_file(sampleFilesPath+"/"+fileName)+"\n")
