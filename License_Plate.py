import requests
import License_Plate
def getLicensePlateNumber(image):
    with open(image, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token 2d858f219e879f4f173f22a619d0e4c70c47a7d1'})
    result=response.json()
    if len(result['results'])==0:
        return 0
    else:
        return result['results'][0]['plate']

'''with open('Detected Images/violation_25.jpg', 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token 2d858f219e879f4f173f22a619d0e4c70c47a7d1'})
result=response.json()

if len(result['results'])==0:
    print(0)
else:
    print(result['results'][0]['plate'])'''
