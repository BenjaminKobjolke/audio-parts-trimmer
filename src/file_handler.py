import os

class FileHandler:
    def get_mp3_files(self, input_folder):
        """Lists all mp3 files in a given directory."""
        try:
            return [f for f in os.listdir(input_folder) if f.endswith(".mp3")]
        except FileNotFoundError:
            print(f"Input folder '{input_folder}' not found.")
            return []

    def create_output_directory(self, output_folder):
        """Creates the output directory if it doesn't exist."""
        if not os.path.exists(output_folder):
            try:
                os.makedirs(output_folder)
            except OSError as e:
                print(f"Error creating output directory: {e}")
