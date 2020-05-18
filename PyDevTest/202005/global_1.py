g_var = 10

def func():
    print('g_var = {}'.format(g_var))

print(__name__)
if __name__ == '__main__':
    func()