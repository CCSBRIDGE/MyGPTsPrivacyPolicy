# -*- coding: utf-8 -*-
# coding=utf-8
# coding: utf-8
# @Time    : 2024/6/30 22:48
# @Author  : Mark Deng
# @Email   : 1114026501@qq.com
# @File    : video2sound
# @Software: PyCharm


from moviepy.editor import VideoFileClip


def extract_audio_from_video(video_path):
    # 加载视频文件
    video = VideoFileClip(video_path)
    # 提取音频
    audio = video.audio
    # 构建音频文件的路径，将视频文件的扩展名改为.mp3
    audio_path = video_path.rsplit('.', 1)[0] + '.mp3'
    # 保存音频文件
    audio.write_audiofile(audio_path)
    print(f"音频已保存至: {audio_path}")


# 示例用法
if __name__ == "__main__":
    video_path = r"D:\HG\内部课(大课）：男神的聊天思维.mp4"
    extract_audio_from_video(video_path)
