import os

import tensorflow_datasets as tfds
from dotenv import load_dotenv

# noinspection PyUnresolvedReferences
import datasets
from datasets.config import SignDatasetConfig

load_dotenv()

config = SignDatasetConfig(name="256x256:10", include_video=True, fps=10, resolution=(256, 256))

# aslg_pc12 = tfds.load('aslg_pc12')
#
# rwth_phoenix2014_t = tfds.load('rwth_phoenix2014_t', builder_kwargs=dict(config=config))

autsl = tfds.load('autsl', builder_kwargs=dict(
    train_decryption_key=os.getenv("AUTSL_TRAIN_DECRYPTION_KEY"),
    valid_decryption_key=os.getenv("AUTSL_VALID_DECRYPTION_KEY")
))

print([d["video"].shape for d in iter(autsl["train"])])