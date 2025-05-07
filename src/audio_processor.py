import os
import random
from pydub import AudioSegment
from .file_handler import FileHandler
from .audio_file import AudioFile

class AudioProcessor:
    def __init__(self, input_folder, output_folder, output_filename, random_sort, segment_length):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.output_filename = output_filename
        self.output_path = os.path.join(self.output_folder, self.output_filename)
        self.random_sort = random_sort
        self.segment_length = segment_length * 1000 # Convert seconds to milliseconds
        self.file_handler = FileHandler()
        self.pause = AudioSegment.silent(duration=1000)  # 1 second pause in milliseconds

    def process_files(self):
        """Orchestrates the audio processing workflow."""
        self.file_handler.create_output_directory(self.output_folder)
        audio_files = self.load_audio_files()
        if not audio_files:
            print(f"No mp3 files found in '{self.input_folder}'.")
            return

        combined_audio = self.combine_audio(audio_files)

        if combined_audio:
            self.export_audio(combined_audio)
            print(f"Successfully created {self.output_filename} in {self.output_folder}")

    def load_audio_files(self):
        """Loads audio files from the input folder."""
        mp3_files = self.file_handler.get_mp3_files(self.input_folder)
        if self.random_sort:
            random.shuffle(mp3_files)
        audio_files = []
        for filename in mp3_files:
            filepath = os.path.join(self.input_folder, filename)
            audio_files.append(AudioFile(filepath, filename))
        return audio_files

    def combine_audio(self, audio_files):
        """Combines the trimmed audio files with pauses."""
        combined_audio = AudioSegment.empty()
        total_files = len(audio_files)
        for i, audio_file in enumerate(audio_files):
            print(f"Processing file {i+1}/{total_files}: {audio_file.filename}")
            try:
                audio = AudioSegment.from_mp3(audio_file.filepath)
                trimmed_audio = audio[:self.segment_length]
                combined_audio += trimmed_audio
                combined_audio += self.pause
            except Exception as e:
                print(f"Error processing {audio_file.filename}: {e}")
        # Remove the last pause if there is one
        if combined_audio.duration_seconds > 0:
            combined_audio = combined_audio[:-1000]
        return combined_audio

    def export_audio(self, combined_audio):
        """Exports the combined audio to the output file."""
        try:
            combined_audio.export(self.output_path, format="mp3")
        except Exception as e:
            print(f"Error exporting audio: {e}")
