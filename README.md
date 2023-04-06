This is a modified version of https://github.com/SociallyIneptWeeb/LanguageLeapAI which uses rinna api for customizable sound profile, which also allow user to use different expression with modifying the following part of the code in request.py in module:
body = {'text': sentence, 'speaker_x': 0.0, 'speaker_y': 0.0, 'style': 'talk'}
modify speaker_x and speaker_y value from -3 to 3 for sound profile and style for expression, you can try those out in http://koeiromap.rinna.jp/ to find your favorite sound profile.
New version now uses whisper without docker or colab by running locally with cpu, run the following command to install the whisper modules:
```
pip install git+https://github.com/openai/whisper.git
```
