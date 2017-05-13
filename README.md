# Watson Speech-to-text with Speaker Diarization

This script `watsonSTT.py` is built on top of the examples provided in the watson-developer-cloud Python SDK repo: [https://github.com/watson-developer-cloud/python-sdk](https://github.com/watson-developer-cloud/python-sdk). The script takes as input a wav file, runs Watson's speech-to-text with speaker diarization, and saves json file with the output. A detailed description of how to interpet the json output, can be found [here](https://www.ibm.com/watson/developercloud/doc/speech-to-text/output.html). 

## Installation
First download the [watson-developer-cloud](https://github.com/watson-developer-cloud/python-sdk#installation) for Python.

```
$ pip install --upgrade watson-developer-cloud
 ```
 
## Running

To run Watson, you will first need a IBM Bluemix account: [https://console.ng.bluemix.net](https://console.ng.bluemix.net). After signing up for free account, you can log on and request to use their Speech to Text API service. Once you add the service (which is free for the first 1,000 minutes) you will receive credentials (USERNAME and PASSWORD).

In the `watsonSTT.py` make sure to replace 'USERNAME' and 'PASSWORD' with your own Bluemix credentials. Then to run the script on a wav file, use:

```
python watsonSTT.py audio_example.wav
```

This will run watson with speaker diarization and save the output to a json file which will have the same name as the audio file, e.g. `audio_example.json`. 

For more details on the watson-developer-cloud and for more script examples, check out that repo: [https://github.com/watson-developer-cloud/python-sdk/blob/master/README.md](https://github.com/watson-developer-cloud/python-sdk/blob/master/README.md). 
