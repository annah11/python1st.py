birthday = {
        'hana':'22/11/2003',
        'namo':'20/10/2003',
        'mon':'12/12/2000'}
name=input('Enter name')
if name in birthday:
    print('mr./miss{} was born on {}'.format(name,birthday[name]))
else:
    print('name not found')

