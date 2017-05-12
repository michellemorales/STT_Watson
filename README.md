# Watson Speech-to-text with Speaker Diarization

This zip file is a copy of the repo provided here: https://github.com/watson-developer-cloud/speech-to-text-websockets-python. The only change made to the code is that this version includes in its output (as default) speakers labels. A detailed description of how to interpet the json output, can be found [here](https://www.ibm.com/watson/developercloud/doc/speech-to-text/output.html). 

## Installation
First download and unzip the file.

```command
 unzip speech-to-text-websockets-python.zip
 ```
In the Watson repo it was noted that certain packages have been observed to conflict with the package requirements for the speech-to-text script, so it is advisable to install the required packages in a separate virtual environment. Install all the required dependencies, like so:

```
cd speech-to-text-websockets-python
pip install -r requirements.txt
```

## Running

To run Watson, you will first need a IBM Bluemix account: [https://console.ng.bluemix.net](https://console.ng.bluemix.net). After signing up for free account, you can log on and request to use their Speech to Text API service. Once you add the service (which is free for the first 1,000 minutes) you will receive credentials (USERNAME and PASSWORD).

Make sure your audio files are in the `recordings/` directory. All json files will be saved to the `output/` directory. Use the following command to run ASR on your audio files:

```
python ./sttClient.py -credentials <username>:<password> -model en-US_BroadbandModel
```

For more details on the `sttClient.py` script see the orginal repo: [https://github.com/watson-developer-cloud/speech-to-text-websockets-python](https://github.com/watson-developer-cloud/speech-to-text-websockets-python).
