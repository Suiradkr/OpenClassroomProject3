from csv_class import CSVWriter
from cluster import Cluster
from vm_data_manager import VMDataManager


def print_clusters_info():

    data_manager = VMDataManager()
    cluster_ids = data_manager.get_all_vm_ids()

    if not cluster_ids:
        print("No VM IDs found to process.")
        return

    print("--- Printing Cluster Information ---")
    all_clusters_data = []
    for cluster_id in cluster_ids:
        cluster_obj = Cluster(cluster_id, data_manager)
        cluster_obj.set_cluster_info()
        all_clusters_data.append(cluster_obj.to_dict())
        print(cluster_obj)

    for item in all_clusters_data:
        print(item)
    print("\n" + "=" * 50 + "\n")

    output_filename = "cluster_report.csv"
    csv_writer = CSVWriter(all_clusters_data, output_filename)
    csv_writer.to_csv()


print_clusters_info()
