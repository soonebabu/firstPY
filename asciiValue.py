import logging
import csv
logging.basicConfig(filename='sample.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

with open('info.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_counter = 0
    for row in csv_reader:
        if line_counter == 0: #It represents the fist row
            print(f'Column names are {", ".join(row)}')
            line_counter += 1 #it avoids double entry in first row
        else:
            logging.info(row[0])
            print(f'\t{row[0]} who is {row[1]} by sex, and was born in {row[2]} {row[3]}.')
            line_counter += 1 #it moves the cursur to next line or row
    print(f'There are  {line_counter} rows of data.')
