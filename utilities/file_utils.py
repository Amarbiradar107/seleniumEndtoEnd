from pathlib import Path


class FileUtils:

    @staticmethod
    def create_folder(folder):

        Path(folder).mkdir(
            parents=True,
            exist_ok=True
        )

    @staticmethod
    def exists(path):

        return Path(path).exists()