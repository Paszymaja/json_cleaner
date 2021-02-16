import json


def main():
    with open('input.json', encoding='utf8') as f:
        data = json.load(f)
    transcript = json_extract(data, "transcript")
    print(transcript)
    save_to_txt(transcript)


def save_to_txt(data):
    with open("data/outfile.txt", "w") as outfile:
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


if __name__ == '__main__':
    main()
