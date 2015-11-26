import os 
import subprocess 

FILE_SYSTEM = '/dev/disk0s2s1'

SIZE_COLUMN = 'Size'
USED_COLUMN = 'Used'
USED_PERCENT_COLUMN = 'Capacity'

INODE_USED_COLUMN = 'iused'
INODE_FREE_COLUMN = 'ifree'
INODE_USED_PERCENT_COLUMN = '%iused'

def table_info_from_command(command, row_start, columns):
	output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]

	header_line = output.split('\n')[0]

	headers = header_line.split()
        indexes = [headers.index(col) for col in columns]


	fs_line = next((line.strip() for line in  output.split('\n') if line.strip().startswith(row_start)), "")

	values = fs_line.split()

	return [values[i] for i in indexes]

print table_info_from_command(["df", "-h"], FILE_SYSTEM, [SIZE_COLUMN, USED_COLUMN, USED_PERCENT_COLUMN])
print table_info_from_command(["df", "-hi"], FILE_SYSTEM, [INODE_USED_COLUMN, INODE_FREE_COLUMN, INODE_USED_PERCENT_COLUMN])

