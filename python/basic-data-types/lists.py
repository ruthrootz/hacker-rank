if __name__ == '__main__':

    current_list = []
    N = int(input())

    for _ in range(0, N):
        command = input()
        split_command = command.split(' ')
        if split_command[0] == 'print':
            print(current_list)
        elif split_command[0] == 'append':
            current_list.append(int(split_command[1]))
        elif split_command[0] == 'remove':
            current_list.remove(int(split_command[1]))
        elif split_command[0] == 'sort':
            current_list.sort()
        elif split_command[0] == 'pop':
            current_list.pop()
        elif split_command[0] == 'reverse':
            current_list.reverse()
        elif split_command[0] == 'insert':
            current_list.insert(int(split_command[1]), int(split_command[2]))
        else:
            print('invalid command')

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
