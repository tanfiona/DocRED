import config
import models
import numpy as np
import os
import time
import datetime
import json
from sklearn.metrics import average_precision_score
import sys
import os
import argparse
# import IPython

# sys.excepthook = IPython.core.ultratb.FormattedTB(mode='Verbose', color_scheme='Linux', call_pdb=1)


parser = argparse.ArgumentParser()
parser.add_argument('--model_name', type = str, default = 'CNN3', help = 'name of the model')
parser.add_argument('--save_name', type = str, default = 'CNN3')

parser.add_argument('--train_prefix', type = str, default = 'train')
parser.add_argument('--test_prefix', type = str, default = 'dev_test')
parser.add_argument('--input_theta', type = float, default = -1)
parser.add_argument('--output_file', type = str, default = "result.json")


args = parser.parse_args()
model = {
	'CNN3': models.CNN3
	# 'LSTM_SP': models.LSTM_SP
}

con = config.Config(args)
# limited gpu ram
con.set_batch_size(10)
#con.load_train_data()
con.load_test_data()
# con.set_train_model()
con.testall(model[args.model_name], args.save_name, args.input_theta)
