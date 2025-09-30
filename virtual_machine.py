class VM:

    def __init__(self, description, clustername, vm_id):
        self.description = description
        self.clustername = clustername
        self.id = vm_id

    def __str__(self):
        return f"VM ID: {self.id}, Description: {self.description}, Cluster Name: {self.clustername}"
