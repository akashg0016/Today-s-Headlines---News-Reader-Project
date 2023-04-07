# AKHBAAR PADH KE SUNAO
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("")

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

querystring = {"targetCalories": "2000", "timeFrame": "day"}

headers = {
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        'x-rapidapi-key': "dfa4634881554bf3b2aac3b11a213140"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)