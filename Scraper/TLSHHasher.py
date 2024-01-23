import os
import tlsh

from IFuzzyHasher import IFuzzyHasher


class TLSHHasher(IFuzzyHasher):
    def hash_binary(self, file_path: os.path) -> str:
        return self._get_hash_from_binary(file_path)

    def __str__(self):
        return "TLSHHasher"

    def _get_hash_from_binary(self, file_path: os.path) -> str:
        try:
            with open(file_path, "rb") as f:
                hashed_data = tlsh.hash(f.read())
                return hashed_data
        except IOError:
            print(f"{file_path} is not readable!")
            raise ValueError(f"{file_path} is not readable!")