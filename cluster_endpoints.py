import json

def all_vms_ids():
    cluster_ids = []
    with open('./data/get_all_vms.json', 'r') as f:
        all_vms = json.load(f)
        for cluster in all_vms:
            cluster_ids.append(cluster['id'])
    return cluster_ids

def get_version(cluster_id):
    with open('./data/get_lc_data.json', 'r') as f:
        lc_data = json.load(f)
        for cluster in lc_data:
            if cluster[0]['deployedvm'] == cluster_id:
                return cluster[1]['version']
        return 'data not found'

def get_podbox(cluster_id):
    with open('./data/get_podbox_data.json', 'r') as f:
        all_podbox = json.load(f)
        for cluster in all_podbox:
            if cluster['id'] == cluster_id:
                return cluster["podbox"]
        return 'data not found'


