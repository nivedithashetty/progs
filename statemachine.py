data=raw_input('enter a no')
print data


STATE_MACHINE={
    's':{'final':False,'transitions':(None,'int',None)},
    'int':{'final':True,'transitions':(None,'int','s1')},
    's1':{'final':False,'transitions':(None,'s2',None)},
    's2':{'final':True,'transitions':(None,'s2',None)},
    None:{'final':False,'transitions':(None,None,None)}}

cur=STATE_MACHINE['s']

for i in data:
    if i.isalpha():
        cur=STATE_MACHINE[cur['transitions'][0]]
    elif i.isdigit():
        cur=STATE_MACHINE[cur['transitions'][1]]
    elif i=='.':
        cur=STATE_MACHINE[cur['transitions'][2]]
    else:
        cur=None
        break
    if cur=={'final':False,'transitions':(None,None,None)}:
        print 'invalid'
        break
if cur['final']:
    print 'valid'

    
