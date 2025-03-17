import argparse
import functools
import time
import os
from infer import car_type_detect
from macls.predict import MAClsPredictor
from macls.utils.record import RecordAudio
from macls.utils.utils import add_arguments, print_arguments

parser = argparse.ArgumentParser(description=__doc__)
add_arg = functools.partial(add_arguments, argparser=parser)
add_arg('configs',          str,    'configs/ecapa_tdnn_ifbeep.yml')
add_arg('use_gpu',          bool,   True)
add_arg('record_seconds',   int,    5)
add_arg('model_path',       str,    'models/EcapaTdnn_MFCC/best_model/')
args = parser.parse_args()
print_arguments(args=args)

# 获取识别器
predictor = MAClsPredictor(configs=args.configs,
                           model_path=args.model_path,
                           use_gpu=args.use_gpu)

record_audio = RecordAudio()
i=0
if __name__ == '__main__':
    print('汽车鸣笛抓拍系统开始运行')
    try:
        while True:
            # 加载数据
            save_path = "save_audio/%s.wav" % str(time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))
            # input(f"按下回车键开机录音，录音{args.record_seconds}秒中：")
            audio_data = record_audio. record(record_seconds=args.record_seconds, save_path=save_path)
            # 获取预测结果
            label, s = predictor.predict(save_path)#, sample_rate=record_audio.sample_rate)
            print(f'预测的标签为：{label}，得分：{s}')
            if (label == 'beep' and s > 0.9):
                car_type_detect(save_path)
            else:
                os.remove(save_path)
    except Exception as e:
        print(e)
