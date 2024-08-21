state_list = ["new south wales", "victoria", "queensland", "south australia", "western australia", "tasmania", "northern territory", "remote"]

def locationClassify(data):
    job_id = data['job_id']
    state_label = None
    city_label = None
    location = data['job_location'].lower()

    for each_state in state_list:
        if each_state in location:
            state_label = each_state
            data['label']['state'] = state_label
            break
    
    return data
