---
layout: default
title: Examples
description: The VoxTube dataset examples
---

## Meta file example and description

Meta information is stored in a per-channel manner in `resources/meta/*.json` files:
```json
{
    "video_id_0": [
        [segment1_start, segment1_end],
        [segment2_start, segment2_end],
        ...,
        [segmentN_start, segmentN_end]
    ],
    "video_id_1": [
        [segment1_start, segment1_end],
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

where the name of .json file is an id of a YouTube channel, and each *segmentX_start* and *segmentX_end* are stamps in seconds, for example

```
# cat UC__gC1TbqcY5j_owWKKUEUQ.json
{"LYdLsl4zJj0": [[114.0, 118.0], [78.0, 82.0], [172.0, 176.0], [302.0, 306.0], [372.0, 376.0], [250.0, 254.0], [22.0, 26.0], [310.0, 314.0], [126.0, 130.0], [204.0, 208.0]], "4arwR9j58BY": [[114.0, 118.0], [220.0, 224.0], [154.0, 158.0], [14.0, 18.0], [224.0, 228.0], [212.0, 216.0], [250.0, 254.0], [346.0, 350.0], [142.0, 146.0], [342.0, 346.0]]...
```


## Wav file example

Please see below a couple of loaded audio samples using the provided metadata


## Data downloading example

The following snippets show how to download the VoxTube data using meta **.json** file

### Pre-requisites

* Install **ffmpeg**, **libsndfile1** and [**yt-dlp**](https://github.com/yt-dlp/yt-dlp) libraries:

```bash
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install ffmpeg libsndfile1

# install python requirements
python3 -m pip install -r requirements.txt
```

* Download required **.json** files by cloning the [VoxTube](https://github.com/IDRnD/VoxTube) repo
```bash
git clone https://github.com/IDRnD/VoxTube.git
```


### Example usage

> Note that in example script by default each audio is converted to 16 kHz sampling frequency **.wav** file when downloading

```bash
# example of downloading using one random .json file
cd VoxTube/examples
python3 load_data.py ../resources/meta/UCFcL4NsBzfWh1bLr6brouWg.json <DATASET_ROOT>
```


[back](./)
