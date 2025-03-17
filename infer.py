import argparse
import functools
import shutil
import os
from mycopy import handleAssetsFile,mycopyfile
from pathlib import Path
from yolov5.detect_car import predict
# from infer_car import  car_type_detect
from macls.predict import MAClsPredictor
from macls.utils.utils import add_arguments, print_arguments
parser = argparse.ArgumentParser(description=__doc__)
add_arg = functools.partial(add_arguments, argparser=parser)
add_arg('configs',          str,    'configs/ecapa_tdnn_ifbeep.yml')
add_arg('use_gpu',          bool,   True)
add_arg('audio_path',       str,    "")
add_arg('model_path',       str,    '')
args = parser.parse_args()
print_arguments(args=args)
output_path = r''
image_path = r'.\yolov5\runs\detect\exp2\crops'
remove_path = r'.\yolov5\runs\detect\exp'
# 获取识别器
predictor = MAClsPredictor(configs=args.configs,
                           model_path=args.model_path,
                           use_gpu=args.use_gpu,
                           )
label, score = predictor.predict(audio_data=args.audio_path)
print(f'音频：{args.audio_path} 的预测结果标签为：{label}，得分：{score}')
def car_type_detect(sound_path):
    label, score = predictor.predict(audio_data=sound_path)
    print(f'音频：{sound_path} 的预测结果标签为：{label}，得分：{score}')
    predict(label)
    dst = os.path.join(os.path.abspath(output_path), str(Path(sound_path).stem))
    os.mkdir(dst)
    handleAssetsFile(image_path, dst + '\\')
    mycopyfile(sound_path, dst + '\\')
    shutil.rmtree(remove_path)
    shutil.rmtree(remove_path +'2')
car_type_detect(args.audio_path)
