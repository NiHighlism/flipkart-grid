from utils import hash_filename, write_wav, read_config
import importlib.util
import os
import sys


DTLN_PATH = read_config(section='Paths')['DTLN_PATH']


def denoise_model(input_folder, output_folder):
    sys.path.append(DTLN_PATH)
    # spec = importlib.util.spec_from_file_location(
    #     "run_evaluation", os.path.join(DTLN_PATH, "run_evaluation.py"))
    # foo = importlib.util.module_from_spec(spec)
    # spec.loader.exec_module(foo)
    # foo.DTLNrunner(input_filename, output_filename, os.path.join(
    #     DTLN_PATH, "pretrained_model/model.h5"))
    from DTLN.run_evaluation import DTLNrunner
    DTLNrunner(
        in_folder=input_folder,
        out_folder=output_folder,
        model=os.path.join(DTLN_PATH, "pretrained_model","model.h5" )
    )


def denoise(input_folder, output_folder):
    cleaned_audio = denoise_model(input_folder, output_folder)
    return