"""
Ranked-Vimeo-90K Dataset Loader

Usage:
    from load_dataset import RankedVimeo90K
    dataset = RankedVimeo90K(root="./Ranked-Vimeo-90K/vimeo_rankmap_swinl")
    seq = dataset[0]  # returns list of 7 numpy arrays (448x256 grayscale)
"""

import os
from PIL import Image
import numpy as np
from torch.utils.data import Dataset


class RankedVimeo90K(Dataset):
    """
    Ranked-Vimeo-90K dataset loader.

    Each sample is a 7-frame video sequence of saliency ranking maps.
    Pixel values represent saliency rank (lower = more salient).

    Args:
        root (str): Path to the vimeo_rankmap_swinl directory.
        transform (callable, optional): Optional transform to apply to each frame.
    """

    def __init__(self, root, transform=None):
        self.root = root
        self.transform = transform
        self.sequences = self._scan_sequences()

    def _scan_sequences(self):
        """Scan all video sequence directories."""
        sequences = []
        for top_dir in sorted(os.listdir(self.root)):
            top_path = os.path.join(self.root, top_dir)
            if not os.path.isdir(top_path):
                continue
            for seq_dir in sorted(os.listdir(top_path)):
                seq_path = os.path.join(top_path, seq_dir)
                if os.path.isdir(seq_path):
                    sequences.append(seq_path)
        return sequences

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, idx):
        """
        Returns:
            frames (list): List of 7 numpy arrays, each shape (256, 448), dtype uint8.
            seq_path (str): Path to the sequence directory.
        """
        seq_path = self.sequences[idx]
        frames = []
        for i in range(1, 8):
            img_path = os.path.join(seq_path, f"im{i}.png")
            img = Image.open(img_path).convert("L")
            arr = np.array(img)
            if self.transform:
                arr = self.transform(arr)
            frames.append(arr)
        return frames, seq_path

    def get_sequence_info(self, idx):
        """Return metadata for a sequence."""
        seq_path = self.sequences[idx]
        rel_path = os.path.relpath(seq_path, self.root)
        top_dir, seq_dir = rel_path.split(os.sep)
        return {
            "index": idx,
            "top_dir": top_dir,
            "seq_dir": seq_dir,
            "path": seq_path,
            "num_frames": 7,
            "resolution": (448, 256)
        }


if __name__ == "__main__":
    # Example usage
    dataset = RankedVimeo90K(root="./vimeo_rankmap_swinl")
    print(f"Total sequences: {len(dataset)}")
    frames, path = dataset[0]
    print(f"First sequence: {path}")
    print(f"Number of frames: {len(frames)}")
    print(f"Frame shape: {frames[0].shape}, dtype: {frames[0].dtype}")
    print(f"Pixel value range: [{frames[0].min()}, {frames[0].max()}]")
