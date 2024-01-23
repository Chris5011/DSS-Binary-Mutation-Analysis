import os

from nilsimsa import Nilsimsa

from IFuzzyHasher import IFuzzyHasher


class NilsimsaHasher(IFuzzyHasher):

    def hash_binary(self, file_path: os.path) -> str:
        return self._get_hash_from_binary(file_path)

    def __str__(self):
        return "NilsimsaHasher"

    def _get_hash_from_binary(self, file_path: os.path) -> str:
        try:
            with open(file_path, "rb") as f:
                nil = Nilsimsa(f.read())
                return nil.hexdigest()
        except IOError:
            print(f"{file_path} is not readable!")
            raise ValueError(f"{file_path} is not readable!")
