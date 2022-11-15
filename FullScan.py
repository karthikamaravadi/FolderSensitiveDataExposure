# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:48:15 2021

@author: SAMARAVADI
"""

import os       # Access the operating system.
#import subprocess

path =("location to scan")

check = ["username","cred", "$cred", "$creds","credentials", "id" , "-Password", "password", "passwd" , "Password", "$username", "$password", "$Password", "$passwd", "USER" ,"USERNAME" ]


def ps1count():
    count=0
    for root, dirs, files in os.walk(path):  
         for filename in files:
            if filename.endswith('.ps1'):
                count+=1
    print("Total powershell scripts found=",+count)          
    

def doccount():
    count=0
    for root, dirs, files in os.walk(path):  
         for filename in files:
            if filename.endswith('.docx') or filename.endswith('.doc'):
                count+=1
    print("Total documents found=",+count)  


def txtcount():
    count=0
    for root, dirs, files in os.walk(path):  
         for filename in files:
            if filename.endswith('.txt'):
                count+=1
    print("Total text files found=",+count)  

def batcount():
    count=0
    for root, dirs, files in os.walk(path):  
         for filename in files:
            if filename.endswith('.bat'):
                count+=1
    print("Total bat files found=",+count)  


def scanps1():
    count=0
    for root, dirs, files in os.walk(path):  
         for filename in files:
             if filename.endswith('.ps1'):
                try:
                     path1 = os.path.abspath(os.path.join(root, filename))
                     command=("Get-Content \""+path1+"\"")
                     #print(command)
                     result=subprocess.run([r'C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe',command],shell=True,stdout=subprocess.PIPE)
                     #print(result.stdout.decode('utf-8')) #"cp1252"
                     splitcontent=(result.stdout.decode('cp1252').split())
                     for word in splitcontent:
                         if word in check:     
                             print("-------------------***************************THE START*******************************---------------------------------")
                             print(path1)
                             print(word,': Found')
                             count+=1
                             print("-------------------***************************THE END*******************************--------------------------------")
                except Exception as e:
                    print(e)
                    pass
    print("Total powershells with creds found=",+count)

def scantxt():
    for root, dirs, files in os.walk(path):  
        for filename in files:
             if filename.endswith('.txt'):
                try:
                    path1 = os.path.abspath(os.path.join(root, filename))
                    print("-------------------***************************THE START*******************************---------------------------------")
                    print(path1)
                    f=open(filename,'r')
                    read = f.read()
                    splitcontent=read.split()
                    for word in splitcontent:
                        if word in check:     
                            print(word,': Found')
                            print("-------------------***************************THE END*******************************--------------------------------")
                except Exception as e:
                    print(e)
                    pass
                
def scanbat():
    for root, dirs, files in os.walk(path):  
         for filename in files:
             if filename.endswith('.bat'):
                try:
                 path1 = os.path.abspath(os.path.join(root, filename))
                 print("-------------------***************************THE START*******************************---------------------------------")
                 print(path1)
                 f=open(filename,'r')
                 read = f.read()
                 splitcontent=read.split()
                 for word in splitcontent:
                     if word in check: 
                         print(word,': Found')
                         print("-------------------***************************THE END*******************************--------------------------------")
                except Exception as e:
                    print(e)
                    pass
                
if __name__ == "__main__":
    ps1count()
    scanps1()
    txtcount()
    scantxt()
    batcount()
    scanbat()
    
    