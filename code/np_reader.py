import numpy as np


class NpManager:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_data(self):
        """Read data from the specified file."""
        if file_path and file_path.endswith('.csv'):
            try:
                data = np.genfromtxt(
                    self.file_path, delimiter=';', names=True, dtype=None, encoding="utf8", autostrip=True
                )
                print(f"Data read successfully. {len(data)} rows found.")
                return data
            except Exception as e:
                print(f"Error reading file {self.file_path}: {e}")
                return None

    def get_calories(self):
        """Get the calories from the data using the `Energ_Kcal` column."""
        if self.data is not None and len(self.data) > 0:
            try:
                # Access the 'Energ_Kcal' column from the structured array
                # print(self.data.dtype.names)
                # p = np.argmax(self.data['Energ_Kcal'])
                calories = np.array([row['Energ_Kcal'] for row in self.data])
                print("Calories extracted successfully.")
                return calories
            except ValueError:
                print("Error: Column 'Energ_Kcal' not found in the data.")
                return None
            except Exception as e:
                print(f"Error processing data: {e}")
                return None
        else:
            print("No data available to process.")
            return None
        
    def process(self):
        """Process the data to extract calories."""
        self.data = self.read_data()
        try:
            if self.data is not None and len(self.data) > 0:
                # Extract calories
                calories = self.get_calories()
                if calories is not None:
                    print("Calories extracted successfully.")
                    max_calories_index = np.argmax(calories)
                    product_with_max_calories = self.data[max_calories_index]
                    max_calories = np.max(calories)
                    max_calories_indices = np.where(calories == max_calories)[0]
                    products_with_max_calories = self.data[max_calories_indices]
                    print(f"Products with max calories: {products_with_max_calories}")
                    for i in products_with_max_calories:
                        if i == products_with_max_calories[-1]:
                            print(i["Shrt_Desc"], i["Energ_Kcal"])
                    print(f"Product with max calories: {product_with_max_calories}")
                else:
                    print("Could not extract calories.")
            else:
                print("No data available to process.")
                return None
        except IndexError:
            print("Error: Data structure does not match expected format.")
            return None
        except Exception as e:
            print(f"Error processing data: {e}")
            return None


if __name__ == "__main__":
    file_path = "ABBREV.csv"

    np_manager = NpManager(file_path)
    np_manager.process()
