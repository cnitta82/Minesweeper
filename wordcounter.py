import time as time


def write_to_file(count):
    with open('journalentry.txt', 'w') as f:
        f.write(count)

while True:
    time.sleep(1)

    with open('journalentry.txt', 'r') as f:
        read_data = f.read()

    if (read_data != '' and (not read_data.isdigit())):
        
        count = len(read_data.split())
        write_to_file(str(count))


