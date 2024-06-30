# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
# @Time    : 2024/6/24 15:07
# @Author  : Mark Deng
# @Email   : 1114026501@qq.com
# @File    : lame2wav
# @Software: PyCharm


import subprocess
import os


def convert_files_in_output_to_wav():
    # 获取当前脚本的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建Output目录的绝对路径
    output_dir = os.path.join(script_dir, './resource/output')

    # 确保Output目录存在
    if not os.path.exists(output_dir):
        print(f"Directory not found: {output_dir}")
        return

    for filename in os.listdir(output_dir):
        if filename.endswith('.lame'):
            lame_path = os.path.join(output_dir, filename)
            wav_path = os.path.join(output_dir, filename.replace('.lame', '.wav'))
            # 构建ffmpeg命令
            cmd = f'ffmpeg -i "{lame_path}" "{wav_path}"'
            try:
                subprocess.run(cmd, check=True, shell=True)
                print(f'Converted {lame_path} to {wav_path}')
            except subprocess.CalledProcessError as e:
                print(f'Error converting {lame_path}: {e}')


if __name__ == '__main__':
    convert_files_in_output_to_wav()
    # ffmpeg -i audio.lame output.wav
