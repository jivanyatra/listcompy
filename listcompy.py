'''Enter your filenames here.'''
large_list = 'testmaster'
small_list = 'testshort'
new_list = 'testoutput'
leftover_list = 'testremainder'

'''Opening files with the proper permissions'''
masterfile = open(large_list, 'r')
shortfile = open(small_list, 'r')
output = open(new_list, 'a')
remainder = open(leftover_list, 'a')

masterlist = []
shortlist = []

'''Importing emails from shortfile into a list'''
for line in shortfile:
    shortlist.append(line.strip().lower())

'''Breaking up masterfile into a list of lines, and
breaking up each line into a list'''
for line in masterfile:
    lr = line.rstrip()
    spl = lr.split(',')
    masterlist.append(spl)

masterfile.close()
shortfile.close()

'''
print masterlist[0]
print masterlist[6]

masterlist[0][3] = 'testing'
masterlist[6][7] = 'testing'

for each in shortlist:
    print each
for each in masterlist:
    print each
'''

for each in masterlist:
    if each[0].lower() in shortlist:
        each[7] = 'p'
        shortlist.remove(each[0].lower())

for each in masterlist:
    output.write(','.join(each) + '\n')

for each in shortlist:
    remainder.write(each + '\n')

output.close()
remainder.close()
