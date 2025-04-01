import os
import sys
import warnings


# Disable logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["ABSL_LOG_QUIET"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Disable warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Fix stderr warnings
stderr_fd = sys.stderr.fileno()
original_stderr = os.dup(stderr_fd)
null_file = open(os.devnull, "w")
os.dup2(null_file.fileno(), stderr_fd)

import tensorflow as tf

os.dup2(original_stderr, stderr_fd)
null_file.close()
