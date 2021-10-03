import json

case1 = {
    "test1":123,
    "test2":{
        "test21":{
            "test211":1,
            "test212":2,
            "test213":0,
            "test214":4,
            "test215":[4,0,1,'-',[0,1,23],'N/A',{'delete_me1':'-','keepme':1,'modify_me2':[1,2,3,0,{'deletem3':0,'hollo':1}]}],
            "tt":{
                "deleteme_list":['-','N/A'],
                'deleteme_item':'-',
                'c':'123'
            }
        },
        "test22":0
    },
    "test3":0
}

filter = {0,'-','N/A'}


def list_handler(llist):
    for w in filter:
        try:
            llist.remove(w)
        except ValueError:
            continue
    for i in range(len(llist)):
        if type(llist[i]) == dict:
            helper(llist[i])
        elif type(llist[i]) == list:
            list_handler(llist[i])

def helper(case):
    keys = list(case.keys())
    for i in range(len(keys)):
        if type(case[keys[i]]) == dict:
            helper(case[keys[i]])
        elif type(case[keys[i]]) == list:
            list_handler(case[keys[i]])       
        else:
            if case[keys[i]] in filter:
                del case[keys[i]]
    


def main():
    helper(case1)
    
    return json.dumps(case1,indent=4)

print(main())