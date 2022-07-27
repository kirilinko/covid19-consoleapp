import requests
import json

class Countries:
  
  def __init__(self):
    self.Confirmed=0
    self.Deaths=0
    self.Under_treatment=0
    self.AllCountries=""
    self.TheCountrie=""
    self.TheCountrie=""
    self.Update_Day=""
    
  def Get_generalStatistic(self):
    url="https://api.covid19api.com/summary"
    response=requests.request("GET",url)
    response=json.loads(response.text)
    self.Confirmed=response['Global']['TotalConfirmed']
    self.Deaths=response['Global']['TotalDeaths']
    self.Under_treatment=self.Confirmed-self.Deaths
    self.Update_Day=response['Date']
    
  def Get_AllCountries(self):
    url="https://api.covid19api.com/summary"
    response=requests.request("GET", url)
    response=json.loads(response.text)
    self.AllCountries=response['Countries']

  def Get_InfoCountry(self, Onecountry):
    self.Get_AllCountries()
    for Countrie in self.AllCountries:
      if Countrie['Country'] == Onecountry.capitalize() :
        self.TheCountrie = Countrie

 