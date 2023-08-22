#!/usr/bin/env python3
import argparse
import multiprocessing as mp
import os
from functools import partial
from pathlib import Path

from tqdm import tqdm

from load_example import download_process_and_cut_channel_videos


def load_json(json_path, dataset_root):
    try:
        download_process_and_cut_channel_videos(
            json_path,
            dataset_root
        )
    except Exception as e:
        print(f'Error while loading channel {json_path}')
        print(f'Exception: {str(e)}')


def main(dataset_root, nj=1):
    # Define default variables
    fwd = os.path.dirname(os.path.realpath(__file__))
    meta_path = Path(f'{fwd}/../resources/meta')
    json_paths = sorted(list(meta_path.glob('*.json')))

    # Run downloading
    load_job = partial(
        load_json,
        dataset_root=dataset_root
    )

    with tqdm(total=len(json_paths)) as pb:
        with mp.Pool(nj) as pool:
            for _ in pool.imap(load_job, json_paths):
                pb.update()

    print(f'Finished loading! Please check {dataset_root}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-r', '--dataset_root', help='Path to store loaded data',
                        required=True, type=str)
    parser.add_argument('-j', '--njobs', help='Number of parallel jobs to run',
                        default=1, type=int, required=False)
    args = parser.parse_args()
    main(args.dataset_root, args.njobs)
