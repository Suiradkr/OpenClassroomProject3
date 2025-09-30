from vm_data_manager import VMDataManager


class Cluster:

    def __init__(self, cluster_id, data_manager: VMDataManager):
        self.id = cluster_id
        self.data_manager = data_manager
        self.podbox = ''
        self.version = ''
        self.created = ''
        self.username = ''
        self.status = ''

    def set_cluster_info(self):
        self.podbox = self.data_manager.get_vm_podbox(self.id)
        self.version = self.data_manager.get_vm_version(self.id)
        self.created = self.data_manager.get_vm_details(self.id, 'created')
        self.username = self.data_manager.get_vm_details(self.id, 'username')
        self.status = self.data_manager.get_vm_details(self.id, 'deployedstatus')

    def __str__(self):
        return (f"Cluster ID: {self.id}, Podbox: {self.podbox}, Version: {self.version}, "
                f"Created: {self.created}, Username: {self.username}, Status: {self.status}")
