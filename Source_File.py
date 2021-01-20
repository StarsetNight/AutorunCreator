# coding = utf-8
import os
import sys


def ud():
    print('================================')
    print('Disk Autorun Editor Version 1.01')
    print('================================')
    init = input('Input the disk drive letter that you want to edit. (Need \\):')
    i1 = input('Input the icon path (Must in the disk that you want to edit! If none, do not input):')
    i2 = input("Input the program's path that you want to be ran automatic:")
    print('Done!')
    os.system('cls')
    print('Creating file...')
    print('[===       ] 30 percent continue')
    edit = open(init + 'autorun.inf', 'a+')
    os.system('cls')
    print('Making file content...')
    print('[=====     ] 50 percent continue')
    if i1 == '':
        content = '''[autorun]
OPEN=''' + i2
    elif i2 == '':
        content = '''[autorun]
ICON=''' + i1
    else:
        content = '''[autorun]
ICON=''' + i1 + '''
OPEN=''' + i2
    os.system('cls')
    print('Writing...')
    print('[========  ] 80 percent continue')
    edit.write(content)
    edit.close()
    os.system('cls')
    print('[==========] 100 percent continue')
    print()
    print('System now needs to restart,\npress Enter to restart, press Ctrl+C to quit.')
    try:
        input()
        os.system('shutdown -s -t 00')
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    ud()
