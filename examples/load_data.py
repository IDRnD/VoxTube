#!/usr/bin/env python3
import argparse
import datetime
import json
import subprocess
import traceback
from pathlib import Path
from typing import List

import soundfile as sf
import yt_dlp
from tqdm import tqdm


# --------------------------------------------------------
#                       Common utils
# --------------------------------------------------------
def run_sh(command: List[str], cwd: str = None):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               cwd=cwd)
    stdout, stderr = process.communicate()
    returncode = process.returncode
    return stdout.decode('utf-8'), stderr.decode('utf-8'), returncode


def format_seconds_to_HHMMSS(seconds: int):
    td = datetime.timedelta(seconds=seconds)
    td_in_seconds = td.total_seconds()
    hours, remainder = divmod(td_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    if minutes < 10:
        minutes = "0{}".format(minutes)
    if seconds < 10:
        seconds = "0{}".format(seconds)
    return "{}:{}:{}".format(hours, minutes, seconds)


# --------------------------------------------------------
#   Define FFmpegPostProcessor (yt_dlp postproc class)
# --------------------------------------------------------
class FFmpegPostProcessor:
    FFMPEG_CMD_TEMPLATE_TO_WAV = "ffmpeg -loglevel panic -i {in_fp} -af "\
     + "aresample=async=1 -ar {samplerate} -ac 1 -y {out_fp}"

    def __init__(
            self,
            # Parameters of output file
            samplerate: int = 16000):
        self.samplerate = samplerate

    def set_downloader(self, dl):
        pass

    def run(self, information):
        try:
            raw_path = Path(information["filepath"])
            if raw_path.suffix == ".part":
                print(f"PARTIAL DOWNLOAD: {raw_path}")
                [str(raw_path)], information

            wav_path = raw_path.with_suffix(".wav")
            ffmpeg_cmd = self.FFMPEG_CMD_TEMPLATE_TO_WAV.format(
                in_fp=str(raw_path),
                out_fp=str(wav_path),
                samplerate=self.samplerate)

            stdout, stderr, returncode = run_sh(ffmpeg_cmd.split())
            if returncode != 0:
                raise Exception(stderr)

            return [str(raw_path)], information
        except Exception as ex:
            print(traceback.format_exc())
            return [str(raw_path)], information


# --------------------------------------------------------
#                 Define main load job
# --------------------------------------------------------
def download_process_and_cut_channel_videos(channel_meta_path, output_root):
    output_root = Path(output_root)
    channel_meta_path = Path(channel_meta_path)
    channel_id = channel_meta_path.stem
    channel_meta = json.loads(channel_meta_path.read_text())

    ydl_opts = {
        'verbose': 0,
        'quiet': True,
        'ignoreerrors': True,
        'skip_download': False,
        'format': 'bestaudio/best',
    }
    for video_id, video_segments_sec in channel_meta.items():
        output_path = output_root / channel_id / video_id
        output_path.parent.mkdir(exist_ok=True, parents=True)
        ydl_opts['outtmpl'] = f'{str(output_path)}.%(ext)s'
        log_fcn = output_path.with_suffix(".err").write_text
        try:
            pp = FFmpegPostProcessor(samplerate=16000)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.add_post_processor(pp, when='post_process')
                download_return_code = ydl.download(video_id)
            if download_return_code:
                error_message = "yt-dlp is unable to make a download of video " \
                     f"{video_id} from channel {channel_id}, please see the " \
                     "script download log. This most likely means that a channel " \
                     "or video doesn't exist anymore. Please check the links " \
                     f"https://www.youtube.com/channel/{channel_id} and " \
                     f"https://www.youtube.com/watch?v={video_id} manually."
                log_fcn(error_message)
                continue
            audio_fp = output_path.with_suffix(".wav")
            output_path.mkdir(exist_ok=True, parents=True)
            if audio_fp.exists():
                samples, sr = sf.read(str(audio_fp))
                for ind, (start_sec,
                          end_sec) in enumerate(tqdm(video_segments_sec)):
                    start = int(start_sec * sr)
                    end = int(end_sec * sr)
                    seg_out_fp = output_path / f"segment_{ind}.wav"
                    sf.write(str(seg_out_fp),
                             samples[start:end],
                             sr,
                             subtype='PCM_16')
            audio_fp.unlink()
        except:
            log_fcn(traceback.format_exc())
            continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("channel_meta",
                        type=Path,
                        help="Channel meta json path.")
    parser.add_argument("output_root",
                        type=Path,
                        help="Target root for dataset")
    args = parser.parse_args()

    download_process_and_cut_channel_videos(args.channel_meta,
                                            args.output_root)
