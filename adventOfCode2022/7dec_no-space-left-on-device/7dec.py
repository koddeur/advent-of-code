def system(file):
    """
    """
    f = open(file, "r")
    line = f.readline()
    file_system={}
    current=None
    i=0
    while(line != '' and i<3):
        if(line[0]=='$') : # is a command line
            print(line)
            line_split = line.split()
            cmd = line_split[1]
            print(cmd)
            if(len(line_split)>2) :
                file_folder_name=line_split[2]
                if(file_folder_name == "/"):
                    print(file_folder_name)
        line = f.readline()
        i+=1
    return True

tree1={'name':'a', 'dad':None ,'children': [{'name':'b', 'dad':'a' ,'children':[]},{'name':'c', 'dad':'a' ,'children':[]}]}

def getNode(node,tree):
    """
    """
    if (node==tree['name']):
        return tree
    else:
        for t in tree['children']:
            getNode(node,t)
