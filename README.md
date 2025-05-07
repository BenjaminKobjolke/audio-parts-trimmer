# Audio Processing Script

This script processes audio files (MP3) from an input folder, trims them to a specified segment length, and combines them into a single output file.

A Python script to process audio files, trim them, and combine them.

## Features

*   **Input Folder:** Specifies the folder containing the MP3 files to process.
*   **Output Folder:** Specifies the folder where the combined audio file will be saved.
*   **Output Filename:** Specifies the name of the output file.
*   **Segment Length:** Specifies the length of each audio segment to be included in the output (in seconds).
*   **Random or Alphabetical Sorting:** Allows sorting of input files randomly or alphabetically.
*   Supports loading a mix of MP3 and OGG files

## How to Run

1.  **Prerequisites:**
    *   Python 3.x
    *   pip install -r requirements.txt

2.  **Run the script:**
    *   Execute the `create_example_output.bat` file.

    or

    *   Run the script directly from the command line: `python main.py [arguments]`

## Command-line Arguments

| Argument          | Description                                                                 | Default Value |
| ----------------- | --------------------------------------------------------------------------- | ------------- |
| `--input_folder`  | Path to the input folder containing MP3 files.                              | `input`       |
| `--output_folder` | Path to the output folder where the combined audio file will be saved.      | `output`      |
| `--output_filename` | The name of the output file.      | `output.mp3`      |
| `--sort_mode`     | Sorting mode for input files (`random` or `alphabetical`).                  | `random`      |
| `--segment_length`| Length of each audio segment in seconds.                                    | `30`          |

## File Structure

```
.
├── .clinerules
├── activate_environment.bat
├── input/
│   ├── ... (MP3 files)
├── main.py
├── output/
│   └── output.mp3
├── process_audio.py
├── README.md
├── requirements.txt
├── src/
│   ├── audio_file.py
│   ├── audio_processor.py
│   └── file_handler.py
└── start.bat
```

## Example

To process audio files from the `input` folder, trim each segment to 15 seconds, sort randomly, and save the output as `output.mp3` in the `output` folder, run:

```bash
python main.py --input_folder input --output_folder output --sort_mode random --output_filename output.mp3 --segment_length 15
