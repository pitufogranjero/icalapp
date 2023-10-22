def writeVariable(file_to_write, value, mode):
    with open(file_to_write, mode) as file:
        # print('Remaining: ' + value)
        file.write(value)
    return True

def readVariable(file_to_read,mode):
    with open(file_to_read, mode) as file:
        # print('Remaining: ' + file.read())
        return file.read()
