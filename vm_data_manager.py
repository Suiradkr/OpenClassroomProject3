import json
import os


class VMDataManager:

    def __init__(self, data_directory='./data'):
        self.data_directory = data_directory
        self._all_vms_file = os.path.join(self.data_directory, 'get_all_vms.json')
        self._lc_data_file = os.path.join(self.data_directory, 'get_lc_data.json')
        self._podbox_data_file = os.path.join(self.data_directory, 'get_podbox_data.json')
        self._get_vm_details_file = os.path.join(self.data_directory, 'get_vm_details.json')

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
                if (isinstance(first_dict, dict) and 'deployedvm' in first_dict
                        and isinstance(second_dict, dict) and 'version' in second_dict):
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

    def get_vm_details(self, vm_id, info):
        vm_details = self._load_json_file(self._get_vm_details_file)
        if vm_details is None:
            return 'data not found'

        for entry in vm_details:
            if isinstance(entry, dict) and 'id' in entry and info in entry:
                if entry['id'] == vm_id:
                    return entry[info]
        return 'data not found'
