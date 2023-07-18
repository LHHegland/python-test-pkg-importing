pkg = 'pkg_z'
mdl = 'mdl_b'

print("Hi! I'm in " + pkg + '.' + mdl + '!')

var_a = "Hi! I'm " + pkg + '.' + mdl + '.var_a!'
var_b = "Hi! I'm " + pkg + '.' + mdl + '.var_b!'
var_z = "Hi! I'm " + pkg + '.' + mdl + '.var_z!'

def fnctn_a(var_n):
    print(var_n + " I'm in " + pkg + '.' + mdl + '.fnctn_a!')

def fnctn_b(var_n):
    print(var_n + " I'm in " + pkg + '.' + mdl + '.fnctn_b!')

def fnctn_z(var_n):
    print(var_n + " I'm in " + pkg + '.' + mdl + '.fnctn_z!')


if __name__ == '__main__':
    fnctn_a(var_a)
    fnctn_b(var_b)
    fnctn_z(var_z)