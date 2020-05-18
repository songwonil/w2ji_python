g_var = 10

def func():
    g_var=20
    print('g_var = {} in fnction'.format(g_var))

print(__name__)
if __name__ == '__main__':
    func()
    print('g_var = {} in main'.format(g_var))