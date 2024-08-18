import os
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from .base import Tokenizer
from .basic import BasicTokenizer
from .regex import RegexTokenizer
from .gpt4 import GPT4Tokenizer
