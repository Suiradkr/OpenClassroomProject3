import json
import os

# Re-using the VMDataManager from the previous step
class VMDataManager:

    def __init__(self, data_directory='./data'):

        self.data_directory = data_directory
        self._all_vms_file = os.path.join(self.data_directory, 'get_all_vms.json')
        self._lc_data_file = os.path.join(self.data_directory, 'get_lc_data.json')
        self._podbox_data_file = os.path.join(self.data_directory, 'get_podbox_data.json')

    def _load_json_file(self, file_path):

        if not os.path.exists(file_path):

            print(f"Error: File not found at {file_path}")
            return None
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {file_path}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while loading {file_path}: {e}")
            return None

    def get_all_vm_ids(self):

        all_vms_data = self._load_json_file(self._all_vms_file)
        if all_vms_data is None:
            return []

        vm_ids = []

        for vm_entry in all_vms_data:
            if isinstance(vm_entry, dict) and 'id' in vm_entry:
                vm_ids.append(vm_entry['id'])
        return vm_ids

    def get_vm_version(self, vm_id):

        lc_data = self._load_json_file(self._lc_data_file)
        if lc_data is None:
            return 'data not found'

        for entry_list in lc_data:
            if isinstance(entry_list, list) and len(entry_list) > 1:
                first_dict = entry_list[0]
                second_dict = entry_list[1]
                if isinstance(first_dict, dict) and 'deployedvm' in first_dict and \
                   isinstance(second_dict, dict) and 'version' in second_dict:
                    if first_dict['deployedvm'] == vm_id:
                        return second_dict['version']
        return 'data not found'

    def get_vm_podbox(self, vm_id):

        all_podbox_data = self._load_json_file(self._podbox_data_file)
        if all_podbox_data is None:
            return 'data not found'

        for podbox_entry in all_podbox_data:
            if isinstance(podbox_entry, dict) and 'id' in podbox_entry and 'podbox' in podbox_entry:
                if podbox_entry['id'] == vm_id:
                    return podbox_entry['podbox']
        return 'data not found'


class Cluster:

    def __init__(self, cluster_id, data_manager: VMDataManager):

        self.id = cluster_id
        self.data_manager = data_manager # Store the data manager instance
        self.podbox = ''
        self.version = ''
        self.created = ''
        self.username = ''
        self.status = ''


    def set_cluster_info(self):

        self.podbox = self.data_manager.get_vm_podbox(self.id)
        self.version = self.data_manager.get_vm_version(self.id)

    def __str__(self):

        return (f"Cluster ID: {self.id}, Podbox: {self.podbox}, Version: {self.version}, "
                f"Created: {self.created}, Username: {self.username}, Status: {self.status}")

class VM:

    def __init__(self, description, clustername, vm_id):

        self.description = description
        self.clustername = clustername
        self.id = vm_id

    def __str__(self):
        return f"VM ID: {self.id}, Description: {self.description}, Cluster Name: {self.clustername}"


def print_clusters_info():

    data_manager = VMDataManager()

    cluster_ids = data_manager.get_all_vm_ids()

    if not cluster_ids:
        print("No VM IDs found to process.")
        return

    print("--- Printing Cluster Information ---")
    for cluster_id in cluster_ids:
        # Create a Cluster object, passing the data manager instance
        cluster_obj = Cluster(cluster_id, data_manager)
        # Fetch the specific info for this cluster
        cluster_obj.set_cluster_info()
        print(cluster_obj)

print_clusters_info()