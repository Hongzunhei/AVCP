import argparse
import functools
import shutil
import os
from mycopy import handleAssetsFile,mycopyfile
from pathlib import Path
from yolov5.detect_car import predict
from macls.predict import MAClsPredictor
from macls.utils.utils import add_arguments, print_arguments
parser = argparse.ArgumentParser(description=__doc__)
add_arg = functools.partial(add_arguments, argparser=parser)
add_arg('configs',          str,    'configs/ecapa_tdnn_car_type.yml')
add_arg('use_gpu',          bool,   True)
add_arg('audio_path',       str,    r"")
add_arg('model_path',       str,    '')
args = parser.parse_args()
print_arguments(args=args)
# 获取识别器
predictor = MAClsPredictor(configs=args.configs,
                           model_path=args.model_path,
                           use_gpu=args.use_gpu,
                           )

# def car_type_detect(sound_path):
#     label, score = predictor.predict(audio_data=sound_path)
#     print(f'音频：{sound_path} 的预测结果标签为：{label}，得分：{score}')

path =r'C:\Users\康俊熙\Desktop\鸣笛识别\car_classfication\AudioClassification-Pytorch-master\test_datasets\Toyota_corolla'
for file_name in os.listdir(path):
    # print('.' in file_name)
    # if '.' in file_name:
    file_path = os.path.join(path, file_name)
    print(file_path)
    label, score = predictor.predict(audio_data=file_path)
    print(f'音频：{file_path} 的预测结果标签为：{label}，得分：{score}')