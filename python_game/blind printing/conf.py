import os.path

COLOR_INACTIVE = (155, 200, 215)
COLOR_ACTIVE = (20, 180, 250)
COLOR_RED = (120, 0, 0)
COLOR_GREEN = (0, 102, 0)
completed_lvl = []
data = {}
param = ['average_speed', 'average_speed_col', 'time_min']


def creat():
    file = open("conf.txt", "w")
    for line in data:
        file.write('{}={}\n'.format(str(line), str(data[line])))
    file.write('completed_lvl=')
    for line in completed_lvl:
        file.write('{},'.format(line))
    file.close()


if os.path.exists("conf.txt"):
    file = open("conf.txt", "r")
    for line in file:
        line = line.replace('\n', '')
        line = line.split("=")
        if line[0] in param:
            data[line[0]] = float(line[1])
        elif line[0] == 'completed_lvl':
            lvl = line[1].split(",")
            lvl.remove('')
            for i in lvl:
                completed_lvl.append(False if i == "False" else True)
    if len(param) == len(data):
        pass
    else:
        for line in param:
            if not line in data:
                data[line] = 0
    file.close()
else:
    for line in param:
        data[line] = 0
    for i in range(15):
        completed_lvl.append(False)
creat()
