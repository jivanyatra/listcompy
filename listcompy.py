'''Enter your filenames here.'''
large_list = 'testmaster'
small_list = 'testshort'
new_list = 'testoutput'

'''Opening files with the proper permissions'''
masterfile = open(large_list, 'r')
shortfile = open(small_list, 'r')
#output = open(new_list, 'w')

masterlist = []
shortlist = []

'''Importing emails from shortfile into a list'''
for line in shortfile:
    shortlist.append(line.strip())

'''Breaking up masterfile into a list of lines, and
breaking up each line into a list'''
for line in masterfile:
    lr = line.rstrip()
    spl = lr.split(',')
    masterlist.append(spl)

masterfile.close()
shortfile.close()

for each in shortlist:
    print each
for each in masterlist:
    print each
