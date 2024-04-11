# project-PodRecord
PodRecord is a simple voice recording software developed in Python.
# Here we go......

# Features:
  Record audio from your microphone
  
  Save recordings in WAV format
  
  Convert audio files to text using AssemblyAI's speech-to-text API
  
  Store transcription data in a SQLite database
  
  Play recorded audio files
  
  Open and play existing audio files

# Requirements

  Python 3.x
  sounddevice library
  soundfile library
  assemblyai library
  playsound library
  tkinter library (usually included in Python installations)
  AssemblyAI API key (get it from [AssemblyAI](https://www.assemblyai.com/app))


# Installation
Clone the repository:
```sh
git clone https://github.com/your-username/PodRecord.git
```

Install the required Python libraries:
```sh
pip install sounddevice soundfile assemblyai playsound tk datetime

```
OR BY/

```sh
Pip install sounddevice
Pip install soundfile
Pip install tk
Pip install datetime
Pip install playsound==1.2
pip install assemblyai
```
open the cloned data
and add your AssemblyAI APi Key into API_Key.py
then:
```sh
  cd <folder name>
```
and run by,
```sh
    python main.py
 ```
    Click on "Record Audio" to start recording.
    Click on "Stop Recording" to stop recording.
    Click on "AUD_ToText" to convert the recorded audio to text.
    Click on "play(Open File)" to open and play an existing audio file.

# Database
Recorded audio files and their transcriptions are stored in a SQLite database named `credentials.db` in the `Outputs` folder.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Shubham-bit-hash/podRecord/blob/main/LICENSE.txt) file for details.






    
