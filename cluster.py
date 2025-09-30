from vm_data_manager import VMDataManager
from datetime import datetime, timezone


class Cluster:

    def __init__(self, cluster_id, data_manager: VMDataManager):
        self.id = cluster_id
        self.data_manager = data_manager
        self.podbox = ''
        self.version = ''
        self.created = ''
        self.username = ''
        self.status = ''

    def format_time(self, created_time):
        dt_object_naive = datetime.fromisoformat(created_time.replace('Z', ''))
        dt_object_utc = dt_object_naive.replace(tzinfo=timezone.utc)
        return dt_object_utc.strftime("%d/%m/%Y %I:%M %p UTC")

    def set_cluster_info(self):
        self.podbox = self.data_manager.get_vm_podbox(self.id)
        self.version = self.data_manager.get_vm_version(self.id)
        self.created = self.format_time(
            self.data_manager.get_vm_details(self.id, 'created'))
        self.username = self.data_manager.get_vm_details(self.id, 'username')
        self.status = self.data_manager.get_vm_details(
            self.id, 'deployedstatus')

    def to_dict(self):

        return {
            "Cluster ID": self.id,
            "Podbox": self.podbox,
            "Version": self.version,
            "Created": self.created,
            "Username": self.username,
            "Status": self.status
        }

    def __str__(self):

        return (f"Cluster ID: {self.id}, Podbox: {self.podbox}, "
                f"Version: {self.version}, Created: {self.created}, "
                f"Username: {self.username}, Status: {self.status}")
