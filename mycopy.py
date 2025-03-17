import os
import shutil
from glob import glob


def mycopyfile(srcfile, dstpath):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)
        shutil.copy(srcfile, dstpath + fname)
        print("copy %s -> %s" % (srcfile, dstpath + fname))

def handleAssetsFile(path, path1):
    if os.path.exists(path1):
        shutil.rmtree(path1)
    shutil.copytree(path, path1)
