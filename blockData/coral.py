import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    name = share.name
    #
    if name == 'minecraft:coral' or name == 'minecraft:coral_fan' or name == 'minecraft:coral_fan_dead' or name == 'minecraft:coral_block':
        type = share.ans["coral_color:8"]
    else:
        type = None
    #
    if name == 'minecraft:coral' or name == 'minecraft:coral_fan_hang' or name == 'minecraft:coral_fan_hang2' or name == 'minecraft:coral_fan_hang3' or name == 'minecraft:coral_block':
        dead_bit = share.ans["dead_bit:1"]
    else:
        dead_bit = None
    #
    if name == 'minecraft:coral_fan_hang' or name == 'minecraft:coral_fan_hang2' or name == 'minecraft:coral_fan_hang3':
        coral_direction = share.ans["coral_direction:3"]
        coral_hang_type_bit = share.ans["coral_hang_type_bit:1"]
    else:
        coral_hang_type_bit = None
        coral_direction = None
    #
    if name == 'minecraft:coral' or name == 'minecraft:coral_block':
        if type == 'blue':
            data = 0
        if type == 'pink':
            data = 1
        if type == 'purple':
            data = 2
        if type == 'red':
            data = 3
        if type == 'yellow':
            data = 4
        #
        if dead_bit == 1:
            return data + 8
        else:
            return data
        #
    #
    if name == 'minecraft:coral_fan' or name == 'minecraft:coral_fan_dead':
        if type == 'blue':
            return 0
        if type == 'pink':
            return 1
        if type == 'purple':
            return 2
        if type == 'red':
            return 3
        if type == 'yellow':
            return 4
        #
    #
    if name == 'minecraft:coral_fan_hang' or name == 'minecraft:coral_fan_hang2' or name == 'minecraft:coral_fan_hang3':
        if dead_bit == 1:
            coral_hang_type_bit = coral_hang_type_bit + 2
        return coral_hang_type_bit + coral_direction * 4
    #