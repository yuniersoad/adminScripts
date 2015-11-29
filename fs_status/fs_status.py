import os 
import subprocess 

FILE_SYSTEM = '/dev/xvda1'

SIZE_COLUMN = 'Size'
USED_COLUMN = 'Used'
USED_PERCENT_COLUMN = 'Use%'

INODE_SIZE_COLUMN = 'Inodes'
INODE_USED_COLUMN = 'IUsed'
INODE_USED_PERCENT_COLUMN = 'IUse%'

def table_info_from_command(command, row_start, columns):
	output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]

	header_line = output.split('\n')[0]

	headers = header_line.split()
        indexes = [headers.index(col) for col in columns]


	fs_line = next((line.strip() for line in  output.split('\n') if line.strip().startswith(row_start)), "")

	values = fs_line.split()

	return [values[i] for i in indexes]

usage_info = table_info_from_command(["df", "-h"], FILE_SYSTEM, [SIZE_COLUMN, USED_COLUMN, USED_PERCENT_COLUMN])
inode_usage_info = table_info_from_command(["df", "-hi"], FILE_SYSTEM, [INODE_SIZE_COLUMN, INODE_USED_COLUMN, INODE_USED_PERCENT_COLUMN])

output = '''<p>Storage Usage: %s/%s  %s</p>
<p>Inode Usage: %s/%s  %s</p>
''' % (usage_info[1], usage_info[0], usage_info[2], inode_usage_info[1], inode_usage_info[0], inode_usage_info[2])
print output 

