import json


# NOTE. course_info.json should always contain the .json of specific course and
# currently this means you have to manually copy n paste .json from labtool
# to course_info.json-file.

def main():

    with open('course_info.json') as data_file:
        data = json.load(data_file)

    write_buffer = ""
    f = open('result.txt', 'w')

    for data_block in data:
        write_buffer = write_buffer + data_block['repository'] + "\n"

    f.write(write_buffer)

if __name__ == '__main__':
    main()