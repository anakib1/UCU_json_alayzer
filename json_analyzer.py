import json

def proceed(path):
    """
    Function shows contents of json file located in <path>. If file does not exist returns exit code 1.
    """
    try:
        f = open(path)
        data = json.load(f)
        while True:
            if isinstance(data, list):
                print(f'Input index of list you would like to view. Index may lay in range [{0} ; {len(data) - 1}]')
                s = input()
                while not s.isnumeric() or int(s) >= len(data):
                    print('Input correct index please')
                    s = input()
                data = data[int(s)]
            elif isinstance(data, dict):
                print('Print key tou would like to view')
                print(f'Keys: {list(data.keys())}')
                s = input()
                while not s in data.keys():
                    print('Input correct key please')
                    s = input()
                data = data[s]
            else:
                print(f'Your object value is: {data}')
                return 0
    except:
        print('Please use correct path')
        return 1
    
