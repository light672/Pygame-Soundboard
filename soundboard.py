import os
import sys
import shutil

inputdevice = 'VoiceMeeter Input (VB-Audio VoiceMeeter VAIO)'

sound_files = "Type the number of the sound file you want to use in your soundboard \n ----------------- \n"
sound_files_array = []

for index in range(0, len(os.listdir())):
    directory = os.listdir()[index]
    if directory.endswith('.wav') or directory.endswith('.mp3'):
        sound_files_array.append(index)

for index in range(0,len(sound_files_array)):
    sound_files +=  str(index) + ': ' + os.listdir()[sound_files_array[index]] + '\n'

print(sound_files)

selection = input()

if int(selection) >= len(sound_files_array):
    print("ERROR: Number out of bounds")
    exit()

sound_name = os.listdir()[sound_files_array[int(selection)]]
new_folder_name = os.listdir()[sound_files_array[int(selection)]].split('.')[0]

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)


new_folder = os.path.join(script_dir, new_folder_name)
try:
    os.mkdir(new_folder)


    

    shutil.move(sound_name, new_folder + "/" + sound_name)

    new_python_script = open(new_folder + "/" + 'soundboard.py', "a")
    new_python_script.write("from pygame import mixer\nmixer.init(devicename='" + inputdevice + "')\nmixer.music.load('" + sound_name + "')\nmixer.music.play()\nwhile mixer.music.get_busy():\n   pass")
    new_python_script.close()

    new_batch_script = open(new_folder + "/" + 'soundboard.bat', "a")
    new_batch_script.write("python soundboard.py")
    new_batch_script.close




     
except FileExistsError as e:
    if "Cannot create a file when that file already exists" in str(e):
        print("Folder already exists.")
    else:
        raise e
