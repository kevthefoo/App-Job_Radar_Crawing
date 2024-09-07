state_list = {
    "new south wales": {"state": "new south wales", "city": ["sydney", "newcastle", "wollongong"]},
    "victoria": {"state": "victoria", "city": ["melbourne"]},
    "queensland": {"state": "queensland", "city": ["brisbane", "gold coast", "cairns"]},
    "south australia": {"state": "south australia", "city": ["adelaide"]},
    "western australia": {"state": "western australia", "city": ["perth"]},
    "tasmania": {"state": "tasmania", "city": ["hobart"]},
    "northern territory": {"state": "northern territory", "city": ["darwin"]},
    "remote": {"state": "remote", "city": ["remote"]},
    "nsw": {"state": "new south wales", "city": ["sydney", "newcastle", "wollongong"]},
    "vic": {"state": "victoria", "city": ["melbourne"]},
    "qld": {"state": "queensland", "city": ["brisbane", "gold coast", "cairns"]},
    "sa": {"state": "south australia", "city": ["adelaide"]},
    "wa": {"state": "western australia", "city": ["perth"]},
    "tas": {"state": "tasmania", "city": ["hobart"]},
    "nt": {"state": "northern territory", "city": ["darwin"]},
    "act": {"state": "australian capital territory", "city": ["canberra"]},
}
              

def locationClassify(data):
    job_id = data['job_id']
    state_label = None
    city_label = None
    location = data['job_location'].lower()

    for each_state in state_list:
        if each_state in location:
            state_label = state_list[each_state]["state"]
            data['label']['state'] = state_label
            break
    
    return data

