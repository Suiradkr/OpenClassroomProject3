from cluster_endpoints import get_podbox, get_version, all_vms_ids


class Cluster:
    def __init__(self, cluster_id):
        self.id = cluster_id
        self.podbox = ''
        self.version = ''
        self.created = ''
        self.username = ''
        self.status = ''

    def set_cluster_info(self):
        self.podbox = get_podbox(self.id)
        self.version = get_version(self.id)


    def __str__(self):
        self.set_cluster_info()
        return f"{self.id, self.podbox, self.version, self.created, self.username, self.status}"

class VM:
    def __init__(self, description, clustername, cluster_id):
        self.description = description
        self.clustername = clustername
        self.id = cluster_id

class LCData:
    def __init__(self):

def print_clusters():
    clusters = all_vms_ids()
    for cluster in clusters:
        vm = Cluster(cluster)
        print(vm)
print_clusters()