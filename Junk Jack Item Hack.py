import re

new_file_handle = open("new.txt", "r")
new_file = new_file_handle.read()
new_file_handle.close()

old_file_handle = open("old.txt", "r")
old_file = old_file_handle.read()
old_file_handle.close()

def mkchar():
            #to do: save to chardata files
    to_find = '''
    "name": "(.+?)",
    "id": (.+?),
    "variants": (.+?),
    .*?
    "stackable": (.+?),
    "kind": "(.+?)",
    '''
    
    a = re.findall(to_find, new_file, re.DOTALL)
    b = [] #in hex values
    c = [] #in completed code form (0000 0000 0000 0000 0000)
    d = [] #sets of 44
    e = [] #fixed sets of 44

    # a -> b
    for key in a:
        b.append((key[0] , hex(int(key[1])) , key[2] , key[3] , key[4]))
    #end a -> b

    # b -> c
    for key in b:
        z = key[1]
        z = z[2:]
        if (len(z) == 1):
            z = '0' + z + '00'
        elif (len(z) == 2):
            z = z + '00'
        elif (len(z) == 3):
            y = z[0]
            z = z[1:]
            z = z + '0' + y
        else:
            print ('fail for:' ,z)
            break    
        y = key[4]
        if (y == 'equippable'):
            y = '0500'
        else:
            y = '0000'
        if (key[3] == 'true'):
            t = 1
        else:
            t = int(key[2])
        s = 0
        while(t != 0):
            if (s == 0):
                r = '0000'
            else:
                r = '0' + str(s)
            c.append((z + r + 'FEFF' + y + '0000'))
            t -= 1
            s += 100
    #end b -> c

    # c -> d
    done = 0
    x = []
    for key in c:
        if (done == 44):
            d.append(x)
            x = []
            done = 0
            x.append(key)
            done +=1
        else:
            x.append(key)
            done +=1
    d.append(x)
    #end c -> d

    # d -> e
    u = len(d)
    w = 0
    while (u !=0):
        v = ''
        for key in d[w]:
            v = v + key
        e.append(v)
        w += 1
        u -= 1
    #end d -> e

    temp = 1
    for key in e:
        print(temp , ':   ' , key , '\n')
        temp += 1

def locdif():
    global a,b,c,d,e,f,g,h
    to_find = '''
    "name": "(.+?)",
    "id": (.+?),
    "variants": (.+?),
    .*?
    "stackable": (.+?),
    "kind": "(.+?)",
    '''

    a = re.findall(to_find, new_file, re.DOTALL)
    b = [] #in hex values
    c = [] #in completed code form (0000 0000 0000 0000 0000)
    d = [] #sets of 44
    e = [] #fixed sets of 44
    f = re.findall(to_find, old_file, re.DOTALL)
    g = [] # in new not in old
    h = [] # in old not in new


    for key in a:
        if (key in f):
            continue
        else:
            g.append(key)

    for key in f:
        if (key in a):
            continue
        else:
            h.append(key)

    if (len(g) != 0):
        print('New Items')
        print('Show New Items?')
        temp = input()
        if (temp == 'y'):
            # g -> b
            for key in g:
                b.append((key[0] , hex(int(key[1])) , key[2] , key[3] , key[4]))
            #end g -> b

            # b -> c
            for key in b:
                z = key[1]
                z = z[2:]
                if (len(z) == 1):
                    z = '0' + z + '00'
                elif (len(z) == 2):
                    z = z + '00'
                elif (len(z) == 3):
                    y = z[0]
                    z = z[1:]
                    z = z + '0' + y
                else:
                    print ('fail for:' ,z)
                    break    
                y = key[4]
                if (y == 'equippable'):
                    y = '0500'
                else:
                    y = '0000'
                if (key[3] == 'true'):
                    t = 1
                else:
                    t = int(key[2])
                s = 0
                while(t != 0):
                    if (s == 0):
                        r = '0000'
                    else:
                        r = '0' + str(s)
                    c.append((z + r + 'FEFF' + y + '0000'))
                    t -= 1
                    s += 100
            #end b -> c

            # c -> d
            done = 0
            x = []
            for key in c:
                if (done == 44):
                    d.append(x)
                    x = []
                    done = 0
                    x.append(key)
                    done +=1
                else:
                    x.append(key)
                    done +=1
            d.append(x)
            #end c -> d

            # d -> e
            u = len(d)
            w = 0
            while (u !=0):
                v = ''
                for key in d[w]:
                    v = v + key
                e.append(v)
                w += 1
                u -= 1
            #end d -> e

            temp = 1
            for key in e:
                print(temp , ':   ' , key , '\n')
                temp += 1
        else:
            None

    else:
        print('No New Items')

    if (len(h) != 0):
        print('Items Deleted:')
        for key in h:
            print (key[0])
    else:
        print('No Items Deleted')
