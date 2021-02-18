import json
import os
import easygui


def main(files):
    number = 0
    for file in files:
        with open(file, encoding='utf8') as f:
            data = json.load(f)
        transcript = json_extract(data, "transcript")
        print(transcript)
        number += 1
        save_to_txt(transcript, number)


def save_to_txt(data, file_number):
    path = ('data/outfile' + str(file_number) + '.txt')
    with open(path, "w") as outfile:
        outfile.write("\n".join(data))


def json_extract(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values


def ChoseFile():
    chose_opiton = easygui.buttonbox(msg='Chose if you want to clean one file or all from directory:',
                                     title='Chose option', choices=['directory', 'files'])
    if chose_opiton == "directory":

        directory = easygui.diropenbox(title="Chose directory")
        files = os.listdir(directory)

        files = [i for i in files if i.endswith('.json')]
    else:
        files = easygui.fileopenbox(title='Chose json files', filetypes=['*.json'], multiple=True)

    return files


if __name__ == '__main__':
    path = ChoseFile()
    main(path)
