---
layout: default
title: The VoxTube Dataset
description: A multilingual speaker recognition dataset by ID R&D Inc.
---

The VoxTube dataset is delivered in the form of YouTube URLs and corresponding meta information per video containing filtered segments with a human speech.

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


## Example of dataset segments

Please see below a couple of downloaded and cut audio samples using the provided metadata and scripts.

| spk_id                   | video_id    | seg_id | audio                                                                        |
|:-------------------------|:------------|:-------|:-----------------------------------------------------------------------------|
| UC--EryqEbhW-VtG80N21TdA | 0GSmioPWEQo | 8      | <a href="http://www.youtube.com/watch?feature=player_embedded&v=0GSmioPWEQo?start=138&end=142" target="_blank"><img src="http://img.youtube.com/vi/0GSmioPWEQo/0.jpg" alt="Speaker UC--EryqEbhW-VtG80N21TdA, example 1" width="240" height="180" border="10" /></a>  |
| UC--EryqEbhW-VtG80N21TdA | 0GSmioPWEQo | 15     | [Play](../resources/audio/UC--EryqEbhW-VtG80N21TdA/0GSmioPWEQo/segment_15.wav) |
| UC--EryqEbhW-VtG80N21TdA | a_CZzxUqKrY | 2      | [Play](../resources/audio/UC--EryqEbhW-VtG80N21TdA/a_CZzxUqKrY/segment_2.wav)  |
| UC--EryqEbhW-VtG80N21TdA | a_CZzxUqKrY | 24     | [Play](../resources/audio/UC--EryqEbhW-VtG80N21TdA/a_CZzxUqKrY/segment_24.wav) |
|                          |             |        |                                                                                |
| UCzy4jKI1KXgv8NpYzP2Ezaw | 4K03k8nVgp4 | 0      | [Play](../resources/audio/UCzy4jKI1KXgv8NpYzP2Ezaw/4K03k8nVgp4/segment_0.wav)  |
| UCzy4jKI1KXgv8NpYzP2Ezaw | 4K03k8nVgp4 | 6      | [Play](../resources/audio/UCzy4jKI1KXgv8NpYzP2Ezaw/4K03k8nVgp4/segment_6.wav)  |
| UCzy4jKI1KXgv8NpYzP2Ezaw | K4zDtpU435c | 2      | [Play](../resources/audio/UCzy4jKI1KXgv8NpYzP2Ezaw/K4zDtpU435c/segment_2.wav)  |
| UCzy4jKI1KXgv8NpYzP2Ezaw | K4zDtpU435c | 7      | [Play](../resources/audio/UCzy4jKI1KXgv8NpYzP2Ezaw/K4zDtpU435c/segment_7.wav)  |


## Dataset downloading example

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

> Note that by default in example script after downloading each audio is converted to 16 kHz sampling frequency **.wav** file and is split into 4 seconds segments.

```bash
# example of downloading using one random .json file
cd VoxTube/examples
python3 load_data.py ../resources/meta/UCFcL4NsBzfWh1bLr6brouWg.json <DATASET_ROOT>
```


[Main page](../index.md)
