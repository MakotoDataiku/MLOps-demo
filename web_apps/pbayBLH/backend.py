import dataiku
import pandas as pd
import random
import json
import requests



# Example:
# From JavaScript, you can access the defined endpoints using
# getWebAppBackendUrl('first_api_call')

@app.route('/get_predictions/<path:params>')
def get_predictions(params):
    variables_dict = json.loads(params)
    print variables_dict
    prediction = random.randint(0,100)
    
    features = {"features":{}}
    features["features"]["Day_number"] = variables_dict['doy']
    features["features"]["Trap"] = variables_dict['location']
    features["features"]["Tavg"] = variables_dict['temp']
    r = requests.post(variables_dict['endpoint_url'].replace('http:/','http://').replace('https:/','https://'),data = json.dumps(features))
    prediction_dict = json.loads(r.text)
    print r.status_code
    prediction = int(prediction_dict.get('result').get('probas').get('1')*100)
    
    if prediction <40:
        level = "Low"
    elif prediction <70:
        level = "Medium"
    else :
        level = "High"
    
    return json.dumps({"prediction":prediction, "risk":level, "raw":json.dumps(prediction_dict)})