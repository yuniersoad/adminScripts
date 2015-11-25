import os 
import subprocess 

FILE_SYSTEM = '/dev/disk0s2s1'
SIZE_COLUMN = 'Size'
USED_COLUMN = 'Used'
USED_PERCENT_COLUMN = 'Capacity'

def table_info_from_command3(command):
	output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]

	header_line = output.split('\n')[0]

	headers = header_line.split()
	size_index = headers.index(SIZE_COLUMN)
	used_index = headers.index(USED_COLUMN) 
	used_percent_index = headers.index(USED_PERCENT_COLUMN)


	fs_line = next((line.strip() for line in  output.split('\n') if line.strip().startswith(FILE_SYSTEM)), "")

	values = fs_line.split()
	size = values[size_index]
	used = values[used_index]
	used_percent = values[used_percent_index]

	return [size, used, used_percent]

print table_info_from_command3(["df", "-h"])

