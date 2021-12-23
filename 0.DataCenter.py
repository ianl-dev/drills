# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Not max, but unique entries * data center!!

files = sys.stdin
output = []

# which database has what: index of data center: data id it has
log = {}  # e.g. {1: set(1,3,4)}
unique = set()
new_files = list(files)
for i in range(len(new_files)):
    line = new_files[i]
    if i == 0:
        # database
        database = line
    else:
        new_line = ''.join(line[1:]).strip('\n')
        new_line = new_line.split()
        # new_line = new_line.replace(' ', '')
        log[i] = set(new_line)
        unique.update(new_line)

# Define unique (number of unique data ID) and done_count (+1 every time a center is done)

# Check if any center has full copy
done_count = 0
max_len = 0
target = None  # store key
unique_len = len(unique)
for center in log:
    # data IDs
    this_len = len(log[center])
    if log[center] == unique:
        done_count += 1
    # Find the max length one (the center with most IDs)
    if this_len > max_len:
        max_len = this_len
        target = center

# print(unique, log, target)

# Check if early stop is needed
if done_count == database or target == None:
    output = ['done']
    sys.stdout.writelines(output)
else:
    # Things we need to fill
    to_fill = unique - log[target]
    # Fill in the most promising one, and then use it to copy files
    while len(log[target]) != unique_len:
        # Check each other line set, see if any can fill current set
        for key in log:
            if key != target:
                # present in key not in target
                difference = log[key] - log[target]
                for diff in difference:
                    # Add instruction
                    output.append('{} {} {}\n'.format(
                        diff, key, target))  # id, from, to
                    # Add the new needed element to target ids
                    log[target].add(diff)

    # fill in the remaining
    for key in log:
        if key != target:
            # present in target but not in key
            difference = log[target] - log[key]
            for diff in difference:
                # Add instruction
                output.append('{} {} {}\n'.format(
                    diff, target, key))  # id, from, to
    # Indicate finish
    output.append('done')
    sys.stdout.writelines(output)
