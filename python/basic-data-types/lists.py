if __name__ == '__main__':

    N = int(input())

    for _ in range(0, N):
        command = input()
        split_command = command.split(' ')
        if split_command[0] == 'print':
            print('print')
        elif split_command[0] == 'append':
            print('append')
        elif split_command[0] == 'remove':
            print('remove')
        elif split_command[0] == 'sort':
            print('sort')
        elif split_command[0] == 'pop':
            print('pop')
        elif split_command[0] == 'reverse':
            print('reverse')
        elif split_command[0] == 'insert':
            print('insert')
        else:
            print('error')

# sample input:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
