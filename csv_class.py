import csv


class CSVWriter:

    def __init__(self, data, filename="output.csv"):
        if not isinstance(data, list):
            raise TypeError("Data must be a list.")
        self.data = data
        self.filename = filename

    def to_csv(self, headers=None):
        try:
            with open(self.filename, 'w',
                      newline='', encoding='utf-8') as csvfile:
                if not self.data:
                    if headers:
                        writer = csv.writer(csvfile)
                        writer.writerow(headers)
                        print(f"Successfully wrote empty CSV "
                              f"with headers to '{self.filename}'.")
                    else:
                        print(f"Warning: No data and no headers provided. "
                              f"Creating an empty file '{self.filename}'.")
                    return True

                first_row = self.data[0]
                if isinstance(first_row, dict):
                    fieldnames = headers if headers else list(first_row.keys())
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(self.data)
                else:
                    raise TypeError("Data must be a list of dictionaries "
                                    "for this CSVWriter implementation.")

            print(f"Successfully wrote data to '{self.filename}'.")
            return True
        except Exception as e:
            print(f"Error writing to file '{self.filename}': {e}")
            return False
