from input import history

diskSize = 70000000
freeSpaceRequired = 30000000
filesystem = {}
pathParts = []

for line in history.split('\n'):
    if line[0] == '$':  # command
        if line[2:4] == 'cd':
            if line[5:] == '..':
                pathParts.pop()
            else:
                pathParts.append(line[5:])
    else:
        path = '/'.join(pathParts)
        if path not in filesystem:
            filesystem[path] = {'subdirs': [], 'filesSize': 0, 'totalSize': 0}
        if line[:3] == 'dir':
            filesystem[path]['subdirs'].append(f'{path}/{line[4:]}')
        else:
            fileSize = line[:line.index(' ')]
            filesystem[path]['filesSize'] += int(fileSize)


def dfs(path):
    for subdir in filesystem[path]['subdirs']:
        dfs(subdir)
    filesystem[path]['totalSize'] = filesystem[path]['filesSize'] + \
        sum([filesystem[subdir]['totalSize']
            for subdir in filesystem[path]['subdirs']])


dfs('/')

freeSpace = diskSize - filesystem['/']['totalSize']
additionalSpaceNeeded = freeSpaceRequired - freeSpace
print(sorted([filesystem[path]['totalSize']
      for path in filesystem if filesystem[path]['totalSize'] > additionalSpaceNeeded])[0])
