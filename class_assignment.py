# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:41:21 2020

@author: lisa_
"""


#1

file = open("BookInfo.txt", "r")

BookName = []
Name = []

for i in file.readlines():
    for j in range(len(i)):
        if i[j]==",":
            Name.append(i[:j])
            BookName.append(i[j+1:])
            break

for i in range(len(BookName)):
    if i<9:
        print("#0"+str(i+1)+" "+"book author: "+Name[i]+", "+"book title: '"+BookName[i]+"'")
    else:
        print("#"+str(i+1)+" "+"book author: "+Name[i]+", "+"book title: '"+BookName[i]+"'")
file.close()

#2

file_1 = open("BookInfo.txt","r")
file_2 = open("BookInfo_new.txt","w")
BookName = []
for i in file_1.readlines():
    for j in range(len(i)):
        if i[j]==",":
            BookName.append(i[j+1:])
            break
file_1.close()       
for i in range(len(BookName)):
    if i<9:
        file_2.write("#0"+str(i+1)+" "+"book title: "+BookName[i]+" number of copies:"+str(ord(BookName[i][1]))+"\n")
    else:
        file_2.write("#"+str(i+1)+" "+"book title: "+BookName[i]+" number of copies:"+str(ord(BookName[i][1]))+"\n")

file_2.close()

#3
#a
def addNewBook():
    file = open("BookInfo1.txt","a",encoding="UTF-8")
    while True:
        Info = input("Input the author name and book title: ")
        if Info == "":
            print("Please input the author name and book title.")
        else:
            file.write("\n"+Info)
            break
    file.close()
#b
def SearchBookByAuthor():
    file = open("BookInfo1.txt","r",encoding="UTF-8")
    Name = input("Enetr an author name: ")
    Found = False
    for i in file.readlines():
        if i[:len(Name)] == Name and i[:len(Name)]!="":
            print(i[len(Name)+2:-2])
            Found = True
            break
    if Found == False:
        print("Sorry, there is no book by this author.")
    file.close()
#c
while True:
    Num = int(input("""--Add a new book to the text file, press 1
--Search for books written by a given author, press 2
--End the program, press 3
"""))
    if Num == 1:
        addNewBook()
    if Num == 2:
        SearchBookByAuthor()
    if Num == 3:
        break
        
































