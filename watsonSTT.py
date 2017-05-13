import json, sys
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

wav_file = sys.argv[1]
output_json = wav_file.replace('.wav', '.json')

speech_to_text = SpeechToTextV1(
    username='USERNAME',
    password='PASSWORD',
    x_watson_learning_opt_out=True
)

print(json.dumps(speech_to_text.models(), indent=2))

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(wav_file, 'rb') as audio:
    result = speech_to_text.recognize(audio, content_type='audio/wav', timestamps=True,
        word_confidence=True, speaker_labels=True)
    with open(output_json, 'w') as f:
        json.dump(result, f, ensure_ascii=False)
    print(result)
