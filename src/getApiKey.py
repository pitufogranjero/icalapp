def getApiKey(file):

    try:
        with open(file, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("The file", file, "not found. Make sure you have saved the key.")
