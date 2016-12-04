import requests

headers = {'accept': 'audio/wav'}

r = requests.get('https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?text=YOU+ARE+great', auth=('02ddd314-0309-4f40-bbf5-10a567a5f41e', 'gwKGbwdwJ1iE'), headers=headers)

with open('aplay.wav', 'wb') as fd:
    for chunk in r.iter_content(1024):
        fd.write(chunk)
