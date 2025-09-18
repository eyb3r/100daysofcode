import requests
import datetime as dt

pixela_ept = 'https://pixe.la/v1/users'
user_params = {
    'token': 'k39fh39fjgb2kasdln53j3j31',
    'username': 'eyber',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
#response = requests.post(url=pixela_ept, json=user_params)
#print(response.text)

graph_ept = f'{pixela_ept}/{user_params["username"]}/graphs'

graph_cfg = {
    'id': 'test1',
    'name': 'Przyklad',
    'unit': 'min',
    'type': 'int',
    'color': 'shibafu'

}

graph_header = {
    'X-USER-TOKEN': 'k39fh39fjgb2kasdln53j3j31',
}
# response = requests.post(url=graph_ept, json=graph_cfg, headers=graph_header)
# print(response.text)
pixel_data = {
    'date': dt.datetime(year=2024, month=3, day=29).strftime('%Y%m%d'),
    'quantity': '11',
}
# response = requests.post(url=f"{graph_ept}/{graph_cfg['id']}", json=pixel_data, headers=graph_header)
# print(response.text)

response = requests.delete(url=f"{graph_ept}/{graph_cfg['id']}/20240331", headers=graph_header)
print(response.text)
