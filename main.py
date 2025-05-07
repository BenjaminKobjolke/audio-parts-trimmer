import os
import argparse
from src.audio_processor import AudioProcessor

# Create the argument parser
parser = argparse.ArgumentParser(description="Process audio files.")

# Add arguments
parser.add_argument("--input_folder", type=str, default="input", help="Path to the input folder")
parser.add_argument("--output_folder", type=str, default="output", help="Path to the output folder")
parser.add_argument("--sort_mode", type=str, default="random", choices=["random", "alphabetical"], help="Sorting mode (random or alphabetical)")
parser.add_argument("--output_filename", type=str, default="output.mp3", help="Output filename")
parser.add_argument("--segment_length", type=int, default=30, help="Length of each segment in seconds")

# Parse the arguments
args = parser.parse_args()

# Determine sort mode
random_sort = args.sort_mode == "random"

# Create an instance of the AudioProcessor and process the files
audio_processor = AudioProcessor(args.input_folder, args.output_folder, args.output_filename, random_sort, args.segment_length)
audio_processor.process_files()
