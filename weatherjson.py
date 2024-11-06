import json

with open('weather.json') as f:
    jsondata = json.load(f)

currents_json = json.loads(jsondata['CurrentsJson'])

for current in currents_json:
    district = current['District']
    state = current['STATE']
    message = current['Message']
    alert = current.get('Alert', 'No alert')
    color = current.get('Color', 'No color specified')
    issue_date = current.get('Issue Date', 'No issue date specified')

    print(f"District: {district}")
    print(f"State: {state}")
    print(f"Message: {message}")
    print(f"Alert: {alert}")
    print(f"Color: {color}")
    print(f"Issue Date: {issue_date}")

print(f"Latest Currents Date: {jsondata['LatestCurrentsDate']}")