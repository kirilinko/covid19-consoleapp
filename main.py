import os
from Class_Countries import Countries
choice = 0
print(" ")
print("                                    Version 1.0")
print("==================================================")
print("|        Welcome to console API Covid19          |")
print("|------------------------------------------------|")
print("| What are you doing ? Choose the correct number | ")
print("|                                                | ")
print("| 1 - Get Generale statistic of Covid19          | ")
print("| 2 - Get All countries statistic                | ")
print("| 3 - Get Statistic of one countrie              | ")
print("| 4 - Get information about the Application      |")
print("|                                                | ")
print("================================================== ")
print("                            Powered By Franck 2022 ")
print("                      https://github.com/kirilinko ")
print("  ")
print("  ")

while (choice < 1) or (choice > 4):
  choice=input("Please select a number to continue : ")
  choice=int(choice)
  
CountryObj = Countries()

if choice==1:
  print ("Wait for the loading...")
  CountryObj.Get_generalStatistic()
  print (" ")
  print ("   == GENERALE STATISTIC OF COVID19 ==   ")
  print ("-------------------------------------------")
  print ("| Confirmed   |  Deaths  | Under treatment|")
  print ("-------------------------------------------")
  print ("|", CountryObj.Confirmed,"  |",  CountryObj.Deaths," |", CountryObj.Under_treatment,"     |")
  print ("-------------------------------------------")
  print ("                Laste Update : ", CountryObj.Update_Day)

if choice==2:
  print ("Wait for the loading...")
  CountryObj.Get_AllCountries()
  print (" ")
  print ("   == ALL COUNTRIES STATISTICS OF COVID19 ==   ")
 
  for country in CountryObj.AllCountries:
    print ( "           ", country['Country'], "           ")
    print ("-----------------------------------------------")
    print ("| Confirmed   |    Deaths   |  Under treatment |")
    print ("-----------------------------------------------")
    print ("|", country['TotalConfirmed'],"    |        ",  country['TotalDeaths']," |   ", country['TotalConfirmed']-country['TotalDeaths'], "    |")
    print ("-----------------------------------------------")

if choice==3:
  name=input("Enter the name of country ")
  print ("Wait for the loading...")
  CountryObj.Get_InfoCountry(name)
  print (" ")
  print ("   == GENERALE STATISTIC OF ",CountryObj.TheCountrie['Country'] ," ==   ")
  
  print ("  ")
   
  print ("| Confirmed :", CountryObj.TheCountrie['TotalConfirmed'])
  print ("-------------------------")
  print ("| Deaths  :",CountryObj.TheCountrie['TotalDeaths'],"     ")
  print ("----------------------------")
  print ("| Under treatment :", CountryObj.TheCountrie['TotalConfirmed']-CountryObj.TheCountrie['TotalDeaths'],"    ")
  print ("--------------------------")
if choice==4:
  print(" ")
  print("--------------------------------------")
  print("Console Application by Franck da COSTA")
  print("--------------------------------------")
  print(" LinkedIn : https://www.linkedin.com/in/franck-analyste-programmeur/")
  print("==============================================")
  print(" Source Code : https://github.com/kirilinko/covid19-consoleapp ")
  print("==============================================")
  print(" API Data : https://api.covid19api.com/ ")
  