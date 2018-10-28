import api
import os
import sys
import subprocess

from api import Api
from subprocess import call

search_term = sys.argv[1]

answ = Api().get_top_answer(search_term)
print(answ)
