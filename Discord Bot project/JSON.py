#Author: Sami Mnif
import json

'''
s: strike
w: wallet
b: bank account
j: job
'''
file_name = 'example.json'

def add_server(file_name, server_id):
    with open(file_name, "r+") as file:
        data = json.load(file)
        diction = {server_id:{}}
        data.update(diction)
        file.seek(0)
        json.dump(data, file, indent = 4)

def add_member(file_name, server_id, member_id):
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    print(json_object)
    
    json_object[str(server_id)][str(member_id)] = {}
    print(json_object)
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()    

def strike_update(file_name, server_id, member_id, strike):
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    print(json_object)
    
    add_strike(file_name, server_id, member_id)
    json_object[str(server_id)][str(member_id)]['s'] = strike
    print(json_object)
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()     

def server_check(file_name, server_id):
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    if str(server_id) in json_object:
        print ('server exists')
        return
    else:
        add_server(file_name, server_id)
        print ('server added...')
def member_check(file_name, server_id, member_id):
    server_check(file_name, str(server_id))
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    print ('member check')
    if str(member_id) in json_object[str(server_id)]:
        if type(json_object[str(server_id)][str(member_id)]) == dict:
            return json_object[str(server_id)][str(member_id)]['s']
        else:
            x = json_object[str(server_id)][str(member_id)]
            add_member(file_name, server_id, member_id)
            strike_update(file_name, str(server_id), str(member_id),int(x))
            return x
    else:
        add_member(file_name, server_id, member_id)
        add_strike(file_name, server_id, member_id)
        return    0
def add_strike(file_name, server_id, member_id):
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    print(json_object)
    
    json_object[str(server_id)][str(member_id)]['s'] = 0
    print(json_object)
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()
def user_bank(file_name, server_id, member_id):
    member_check(file_name, str(server_id), str(member_id))
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    print ("User bank begin")
    print(json_object)
    
    if 'w' not in json_object[str(server_id)][str(member_id)] and 'b' not in json_object[str(server_id)][str(member_id)]:
        json_object[str(server_id)][str(member_id)]['w'] = 0
        json_object[str(server_id)][str(member_id)]['b'] = 0

    print(json_object)
    print ('User bank end')
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()
    return (json_object[str(server_id)][str(member_id)]['w'], json_object[str(server_id)][str(member_id)]['b'])
    
def add_funds(file_name, server_id, member_id, amount):
    user_bank(file_name, server_id, member_id)
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    print ("Fund begin")
    print(json_object)
    
    json_object[str(server_id)][str(member_id)]['w'] += amount

    print(json_object)
    print ("Fund end")
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close() 
def transfer_funds(file_name, server_id, member_id, amount, fro, to):
    user_bank(file_name, server_id, member_id)
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    print(json_object)
    if json_object[str(server_id)][str(member_id)][fro] < amount or amount == 0:
        return False
    else:
        json_object[str(server_id)][str(member_id)][fro] -= amount
        json_object[str(server_id)][str(member_id)][to] += amount

    print(json_object)
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()
    return True
#def rich(file_name, server_id):
    #a_file = open(file_name, "r")
    #json_object = json.load(a_file)
    #a_file.close()
    #x = dict()
    
    #for i in json_object[str(server_id)]:
        
    #a_file = open(file_name, "w")
    #json.dump(json_object, a_file, indent = 4)
    #a_file.close()    

def add_job(file_name, server_id, member_id, job):
    member_check(file_name, str(server_id), str(member_id))
    user_bank(file_name, server_id, member_id)
    job_check(file_name, server_id, member_id)
    
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    json_object[str(server_id)][str(member_id)]['j'] = job
    
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()    

def remove_job(file_name, server_id, member_id):
    member_check(file_name, str(server_id), str(member_id))
    user_bank(file_name, server_id, member_id)
    job_check(file_name, server_id, member_id)
    
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    json_object[str(server_id)][str(member_id)]['j'] = None
    
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()

def job_check(file_name, server_id, member_id):
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    if 'j' not in json_object[str(server_id)][str(member_id)]:
        json_object[str(server_id)][str(member_id)]['j'] = None
        a_file = open(file_name, "w")
        json.dump(json_object, a_file, indent = 4)
        a_file.close()         
        return None
    else:
        return (json_object[str(server_id)][str(member_id)]['j'])

def add_xp(file_name, server_id, member_id, amount):
    member_check(file_name, str(server_id), str(member_id))
    user_bank(file_name, server_id, member_id)
    job_check(file_name, server_id, member_id)
    xp_check(file_name, server_id, member_id)
    
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    json_object[str(server_id)][str(member_id)]['xp'] += amount
    
    a_file = open(file_name, "w")
    json.dump(json_object, a_file, indent = 4)
    a_file.close()

def xp_check(file_name, server_id, member_id):
    a_file = open(file_name, "r")
    json_object = json.load(a_file)
    a_file.close()
    
    if 'xp' not in json_object[str(server_id)][str(member_id)]:
        json_object[str(server_id)][str(member_id)]['xp'] = 0
        a_file = open(file_name, "w")
        json.dump(json_object, a_file, indent = 4)
        a_file.close()         
        return 0
    else:
        return (json_object[str(server_id)][str(member_id)]['xp'])