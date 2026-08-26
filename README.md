# Ranked-Vimeo-90K

A saliency-ranked video dataset for intelligent perceptual machine video coding.

## Overview

Ranked-Vimeo-90K is a large-scale video dataset with pixel-level saliency ranking maps, derived from the Vimeo-90K septuplet dataset. It provides per-frame saliency ordering for 7-frame video clips, designed for research on saliency-aware video compression, intelligent perceptual coding, and machine vision oriented video transmission.

## Authors

- **Shiping Zhu**
- **Zijian Song**

*Beihang University*

## Dataset Structure

```
vimeo_rankmap_swinl/
├── 00001/
│   ├── 0001/
│   │   ├── im1.png
│   │   ├── im2.png
│   │   ├── ...
│   │   └── im7.png
│   ├── 0002/
│   └── ...
├── 00002/
└── ...
```

- **96** top-level directories
- **64,612** video sequences (7 frames each)
- **452,284** PNG images total
- Image resolution: **448 x 256**
- Format: 8-bit grayscale saliency ranking maps
- Each pixel value represents the saliency rank order within the frame

## Download

The full dataset is hosted on Hugging Face Datasets:

**https://huggingface.co/datasets/spzhu/Ranked-Vimeo-90K**

### Using Hugging Face Hub

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="spzhu/Ranked-Vimeo-90K",
    repo_type="dataset",
    local_dir="./Ranked-Vimeo-90K"
)
```

### Using Git LFS

```bash
git lfs install
git clone https://huggingface.co/datasets/spzhu/Ranked-Vimeo-90K
```

## Usage Example

```python
import os
from PIL import Image
import numpy as np

dataset_root = "./Ranked-Vimeo-90K/vimeo_rankmap_swinl"

# Load a 7-frame sequence
seq_path = os.path.join(dataset_root, "00001", "0001")
frames = []
for i in range(1, 8):
    img = Image.open(os.path.join(seq_path, f"im{i}.png"))
    frames.append(np.array(img))

# frames[i] is a 448x256 grayscale saliency ranking map
# Lower pixel value = higher saliency rank
```

## Citation

If you use this dataset in your research, please cite:

```bibtex
@misc{ranked-vimeo-90k,
  title={Ranked-Vimeo-90K: A Saliency-Ranked Video Dataset for Intelligent Perceptual Video Coding},
  author={Zhu, Shiping and Song, Zijian},
  year={2026},
  howpublished={\url{https://github.com/spzhubuaa/Ranked-Vimeo-90K}}
}
```

## Related Work

This dataset is used in the research framework of saliency-object-ranking based intelligent perceptual machine video coding. The ranking maps are generated using a Swin-Large based saliency detection model.

## License

This dataset is provided for research purposes only. Please refer to the original Vimeo-90K dataset license for terms regarding the source video frames.
