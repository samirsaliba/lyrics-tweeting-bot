import csv
import random
import re

#name of the csv file containing the albums information (not lyrics)
csv_name='albums.csv'

#name of the csv file containing to signal whether the files were modified or not
#if you add any new lyric inside any of the .txt files, change the status csv file
status_name='status.csv'

#name of the lyrics files, without the prefix lyric/ and suffix .txt
albums = ['tcdo', 'lr', 'grad', '808s', 'mbdtf', 'wtt', 'cruel', 'yeezus', 'tlop', 'ye', 'ksg']

def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

def choose_file():
	with open(csv_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		csv_headings = next(csv_reader)
		first_line = next(csv_reader)
		lyrics_total = int(first_line[1])
		lyric_num = random.randint(0, lyrics_total)
		currentsum = 0

		for row in csv_reader:
			print(row)

			lyric = lyric_num - currentsum
			if row == []:
				continue
			elif lyric_num < int(row[2]):
				print('row[2]: ' + str(row[2]))
				return row[0], lyric
			currentsum = int(row[2])

def get_lyric(file_name, index):
	file_name = 'lyrics/' + file_name + '.txt'
	file = open(file_name, "r")
	text = file.read()
	text = split_on_empty_lines(text)
	file.close()
	return text[index]

def update_num_lyrics():
	nums = {}
	total = 0
	index = 0
	for album in albums:
		file_name = 'lyrics/' + album + '.txt' 
		file = open(file_name, "r")
		text = file.read()
		text = split_on_empty_lines(text)
		file.close()
		x = len(text)
		nums[album] = len(text)
		total += x

	with open(csv_name, mode='w') as csv_file:
		fieldnames = ['album', 'numlyrics', 'index']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'album': 'total', 'numlyrics': total, 'index': 0})
		for k,v in nums.items():
			index+=v
			writer.writerow({'album': k, 'numlyrics': v, 'index': index})
			
def check_files_changed():
	with open(status_name) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			if row[0] == 'up-to-date':
				print(row[0] + ' ' + row[1])
				if row[1] == ('yes' or ' yes'):
					return True
				else:
					return False

def update_status_file():
	with open(status_name, mode='w') as csv_file:
		fieldnames = ['one', 'two']
		writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		writer.writerow({'one': "write 'yes' besides the comma after 'up-to-date' to sign the lyric files weren't modified", 'two':"" })
		writer.writerow({'one': "write anything else besides the comma below to sign the lyric files were modified", 'two':"" })
		writer.writerow({'one': "please no blank spaces before/after the 'yes'", 'two':"" })
		writer.writerow({'one': "up-to-date", 'two': 'yes'})
					

def main():
	#check if files were changed
	#if yes, then call update_num_lyrics() and update_status_file() (after lyrics were updated)
	#open file, check total lyrics
	#generate random from 0 to total lyrics
	#check file to see which album does that lyric number fall into
	#open chosen album
	#get chosen lyric
	#tweet

	lyrics_up_to_date = check_files_changed()
	if not lyrics_up_to_date:
		update_num_lyrics(files)
		update_status_file()

	file, lyric_index = choose_file()

	tweet = get_lyric(file, lyric_index)
	print(tweet)


if __name__ == '__main__':
	main()