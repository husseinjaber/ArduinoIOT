import time
import os



while 1:
    file =  open('SubAnswersLinesNotFinal.txt', 'r') 
    data = file.read()
    final = data.replace('NewLine', '\n')
    # words = words.replace('NewItemSaved', ' \n ||||\n  ')
    # words = words.replace(',', ' \n  ')
    # words = words.replace('NewLineHere', '\n')
    # words = words.split("NewLine") 
    # ToFile = " "
    # for x in range(len(words)):
    #     ToFile = ToFile +"---------------------------------------------------------ToSplitData,"
    #     if ToFile == " ":
    #         ToFile = words[x] + "\n\n\n\n\n"
    #     else:
    #         ToFile = ToFile + words[x] + "\n\n\n\n\n"

    # print(ToFile)
    file1 = open("D:/Program Files (x86)/EasyPHP-Devserver-17/eds-www/Arduino/files/SubAnswersLines.txt","w")#write mode 
    file1.write(final) 
    


    time.sleep(1)



