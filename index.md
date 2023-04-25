---
layout: default
title: The VoxTube Dataset
description: A multilingual speaker recognition dataset by ID R&D Inc.
---

The VoxTube is a multilingual speaker recognition dataset collected from  **CC BY 4.0** YouTube videos. It includes more than **5.000 speakers** pronouncing more than **4 million utterances** in more than **10 languages**. The work is conducted by [ID R&D Inc](https://www.idrnd.ai). For the collection and filtering details please see [[1]](#citation).

## Data description

| Dataset properties           | Stats     |
|:-----------------------------|:----------|
| # of POI                     | 5.064     |
| # of videos                  | 308.883   |
| # of segments                | 4.481.060 |
| # of hours                   | 4.979     |
| Avg # of videos per POI      | 61        |
| Avg # of segments per POI    | 885       |
| Avg length of segments (sec) | 4         |

###  Language and gender distributions
![Distributions](./resources/img/lang_gender.png)

## Examples and data downloading

Please go to [examples page](./examples/README.md).


## License

The dataset is licensed under **CC BY-NC-SA 4.0**, please see the [license](LICENSE).

Please note that the provided data is relevant on the February 2023 and the corresponding CC BY 4.0 licenses are valid on that date. ID R&D Inc. is not responsible for changed license type or a video or if the video was deleted. If you have found your channel meta data in this dataset and want to exclude this information, please contact us at www.idrnd.ai/contact.


## Citation

Please cite paper below if you make use of the dataset:

```
[1] I. Yakovlev, A. Okhotnikov, N. Torgashov, R. Makarov, Y. Voevodin, K. Simonchik
VoxTube: a multilingual speaker recognition dataset  
INTERSPEECH, 2023.
```