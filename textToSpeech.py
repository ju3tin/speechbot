import requests


def textToSpeech( sentence ):
    headers = {'accept': 'audio/wav'}
    sentence = sentence.replace(' ', '+')

    r = requests.get('https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?text=' +
                     sentence , auth=('02ddd314-0309-4f40-bbf5-10a567a5f41e', 'gwKGbwdwJ1iE'), 
                     headers=headers)

    with open('aplay.wav', 'wb') as fd:
        for chunk in r.iter_content(1024):
            fd.write(chunk)


if __name__ =='__main__':
    textToSpeech('trial 1 1 2 2 ')
