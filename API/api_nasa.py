import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import wget
pp = PrettyPrinter()


# https://medium.com/daily-python/consuming-nasa-api-using-python-part-1-daily-python-17-4ce104fa47ab
# https://api.nasa.gov/
def fetchAPOD(apiKey):
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2020-04-19'
  params = {
      'api_key':apiKey,
      'date': date,
      'hd':'True'
  }
  response = requests.get(URL_APOD,params=params).json()
#   wget.download(response['hdurl'], "img2.jpg")
  pp.pprint(response)
  

apiKey = 'VqecgAapl1tJVF1Vs5O9bjNUdoamrE6agaH9px3H'

fetchAPOD(apiKey)

