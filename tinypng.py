#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import click
import tinify

tinify.key = "73DPwk22mSg1rHrLwW16J9YknGn07CF9"  # API KEY
version = "1.0.1"  # 版本

# Set to store the paths of images that have already been compressed
compressed_images = set()

# 获取文件夹下的图片数量
def get_image_count(folder_path):
    image_extensions = ['.png', '.jpg', '.jpeg']
    image_count = 0

    for root, dirs, files in os.walk(folder_path):
        for name in files:
            _, file_extension = os.path.splitext(name)
            if file_extension.lower() in image_extensions:
                image_count += 1
    
    return image_count

# 压缩的核心
def compress_core(inputFile, outputFile, img_width):
    source = tinify.from_file(inputFile)
    if img_width != -1:
        resized = source.resize(method="scale", width=img_width)
        resized.to_file(outputFile)
    else:
        source.to_file(outputFile)

# 递归压缩一个文件夹下的图片
def compress_path_recursive(path, width):
    for root, dirs, files in os.walk(path):
        if 'tiny' in dirs:
            dirs.remove('tiny')
        
        if any(file.endswith(('.png', '.jpg', '.jpeg')) for file in files):
            toFullPath = os.path.join(root, "tiny")
            if not os.path.exists(toFullPath):
                os.makedirs(toFullPath)
            else:
                if get_image_count(root) == get_image_count(toFullPath):
                    continue

        for name in files:
            fileName, fileSuffix = os.path.splitext(name)
            if fileSuffix in ['.png', '.jpg', '.jpeg']:
                toFullName = os.path.join(root, "tiny", name)
                if toFullName not in compressed_images:
                    compressed_images.add(toFullName)
                    compress_core(os.path.join(root, name), toFullName, width)

@click.command()
@click.option('-d', "--dir", type=str, default=None, help="被压缩的文件夹")
@click.option('-w', "--width", type=int, default=-1, help="图片宽度，默认不变")
def run(dir, width):
    if dir is not None:
        compress_path_recursive(dir, width)  # 压缩指定目录下的文件
    else:
        compress_path_recursive(os.getcwd(), width)  # 压缩当前目录下的文件

if __name__ == "__main__":
    run()
