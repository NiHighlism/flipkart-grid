from utils import hash_filename, write_wav


def dprnn(input_filename):
    from asteroid.models import DPRNNTasNet
    
    model = DPRNNTasNet.from_pretrained("mpariente/DPRNNTasNet_WHAM!_sepclean")
    model.separate(input_filename)
    return
