---
layout: default
title: The VoxTube Dataset
description: A multilingual speaker recognition dataset by ID R&D Inc.
---

The VoxTube dataset is delivered in the form of YouTube URLs and corresponding meta information per video containing filtered segments with human speech.

**Updated 02.2024**: *HuggingFace datasets* implementation of a VoxTube is available [here](https://huggingface.co/datasets/voice-is-cool/voxtube)

## Meta file example and description

Meta information is stored in a per-channel manner in `resources/meta/*.json` files:
```
{
    "video_id_0": [
        [segment1_start, segment1_end],
        [segment2_start, segment2_end],
        ...,
        [segmentN_start, segmentN_end]
    ],
    ...
    "video_id_N": [
        [segment1_start, segment1_end],
        ...,
        [segmentN_start, segmentN_end]
    ]
}
```

where the name of **.json** file is an *id* of a YouTube channel, json keys are *ids* of YouTube videos and each **segmentX_start** and **segmentX_end** are timestamps in seconds. For example:

```
# cat VoxTube/resources/meta/UC__gC1TbqcY5j_owWKKUEUQ.json
{
    "LYdLsl4zJj0": [
        [114.0, 118.0],
        [78.0, 82.0],
        [172.0, 176.0],
        [302.0, 306.0],
        [372.0, 376.0],
        ...,
        [204.0, 208.0]
    ],
    "4arwR9j58BY": [
        [114.0, 118.0],
        [220.0, 224.0],
        [154.0, 158.0],
        ...,
        [342.0, 346.0]
    ],
    ...
}
```


## Segments examples

Please see below the examples of dataset samples obtained using the provided metadata.

| spk_id                   | video_id    | timestamps | audio                                                                        |
|:-------------------------|:------------|:-----------|:-----------------------------------------------------------------------------|
| UC--EryqEbhW-VtG80N21TdA | 0GSmioPWEQo | [138, 142] | <a href="https://www.youtube.com/embed/0GSmioPWEQo?start=138&end=142" target="_blank"><img src="http://img.youtube.com/vi/0GSmioPWEQo/0.jpg" alt="Speaker UC--EryqEbhW-VtG80N21TdA, example 1" width="160" height="120" border="10" /></a> |
| UC--EryqEbhW-VtG80N21TdA | 0GSmioPWEQo | [324, 328] | <a href="https://www.youtube.com/embed/0GSmioPWEQo?start=324&end=328" target="_blank"><img src="http://img.youtube.com/vi/0GSmioPWEQo/1.jpg" alt="Speaker UC--EryqEbhW-VtG80N21TdA, example 2" width="160" height="120" border="10" /></a> |
| UC--EryqEbhW-VtG80N21TdA | a_CZzxUqKrY | [272, 276] | <a href="https://www.youtube.com/embed/a_CZzxUqKrY?start=272&end=276" target="_blank"><img src="http://img.youtube.com/vi/a_CZzxUqKrY/0.jpg" alt="Speaker UC--EryqEbhW-VtG80N21TdA, example 3" width="160" height="120" border="10" /></a> |
| UCzy4jKI1KXgv8NpYzP2Ezaw | 4K03k8nVgp4 | [476, 480] | <a href="https://www.youtube.com/embed/4K03k8nVgp4?start=476&end=480" target="_blank"><img src="http://img.youtube.com/vi/4K03k8nVgp4/0.jpg" alt="Speaker UCzy4jKI1KXgv8NpYzP2Ezaw, example 1" width="160" height="120" border="10" /></a> |
| UCzy4jKI1KXgv8NpYzP2Ezaw | 4K03k8nVgp4 | [108, 112] | <a href="https://www.youtube.com/embed/4K03k8nVgp4?start=108&end=112" target="_blank"><img src="http://img.youtube.com/vi/4K03k8nVgp4/1.jpg" alt="Speaker UCzy4jKI1KXgv8NpYzP2Ezaw, example 2" width="160" height="120" border="10" /></a> |
| UCzy4jKI1KXgv8NpYzP2Ezaw | K4zDtpU435c | [218, 222] | <a href="https://www.youtube.com/embed/K4zDtpU435c?start=218&end=222" target="_blank"><img src="http://img.youtube.com/vi/K4zDtpU435c/0.jpg" alt="Speaker UCzy4jKI1KXgv8NpYzP2Ezaw, example 3" width="160" height="120" border="10" /></a> |


## Dataset downloading

The following snippets show how to download the VoxTube data using the meta **.json** files.

### Pre-requisites

* Install **ffmpeg** and **libsndfile1**:
```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install ffmpeg libsndfile1
```

* Download required **.json** files by cloning the [VoxTube](https://github.com/IDRnD/VoxTube) repo:
```bash
git clone https://github.com/IDRnD/VoxTube.git
```

* Install Python [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) library:
```bash
cd VoxTube/examples
python3 -m pip install -r requirements.txt
```


### Example usage

> Note that in default example script each audio is converted to 16 kHz sampling frequency **.wav** file and is split into 4-seconds segments.

```bash
cd VoxTube/examples

# example of one speaker downloading using meta .json file
python3 load_example.py ../resources/meta/UC-9GWCoQoMr_ey6AMhClStQ.json <DATASET_ROOT>

# example of downloading the whole dataset in N parallel jobs
# WARNING: you might run into HTTP Error 429 if there are too many requests
# (parallel jobs) used, decrease -j parameter in this case
python3 load_all_examples.py -r <DATASET_ROOT> -j N
```


[Main page](../index.md)
