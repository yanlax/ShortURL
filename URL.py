import pyshorteners
import os
import platform

if platform.system().lower()=="windows":
	os.system("cls")
print ("\033[1;31m╭━━━┳╮╱╭┳━━━┳━━━┳━━━━╮╭╮╱╭┳━━━┳╮\033[1;m")
print ("\033[1;31m┃╭━╮┃┃╱┃┃╭━╮┃╭━╮┃╭╮╭╮┃┃┃╱┃┃╭━╮┃┃\033[1;m")
print ("\033[1;31m┃╰━━┫╰━╯┃┃╱┃┃╰━╯┣╯┃┃╰╯┃┃╱┃┃╰━╯┃┃\033[1;m")
print ("\033[1;31m╰━━╮┃╭━╮┃┃╱┃┃╭╮╭╯╱┃┃╱╱┃┃╱┃┃╭╮╭┫┃╱╭╮\033[1;m")
print ("\033[1;31m┃╰━╯┃┃╱┃┃╰━╯┃┃┃╰╮╱┃┃╱╱┃╰━╯┃┃┃╰┫╰━╯┃\033[1;m")
print ("\033[1;31m╰━━━┻╯╱╰┻━━━┻╯╰━╯╱╰╯╱╱╰━━━┻╯╰━┻━━━╯\033[1;m")
print ("\033[1;31m   By YanLax\033[1;m")

url = input(" URL: ")
n = input(" Выберите сервис ( 1:Os.db, 2:Chilp.it, 3:Da.gd, 4:Is.gd, 5:Qps.ru, 6:TinyURL.com):  ")

if n == str(1):
	s = pyshorteners.Shortener()
	f = s.osdb.short(url)
	print(" Short URL: ",f)
elif n == str(2):
	s = pyshorteners.Shortener()
	short_url = s.chilpit.short(url)
	print(" Short URL: ",short_url)
elif n == str(3):
	s = pyshorteners.Shortener()
	abz = s.dagd.short(url)
	print(" Short URL: ",abz)
elif n == str(4):
	s = pyshorteners.Shortener()
	abv = s.isgd.short(url)
	print(" Short URL: ",abv)
elif n == str(5):
	s = pyshorteners.Shortener()
	abh = s.qpsru.short(url)
	print(" Short URL: ",abh)
elif n == str(6):
	s = pyshorteners.Shortener()
	abk = s.tinyurl.short(url)
	print(" Short URL: ",abk)
else:
    print(' Error ')

input()