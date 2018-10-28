import api
import os
import subprocess

from api import Api
from subprocess import call

search_term = "git reset"

answ = Api().get_top_answer(search_term)
print(answ)
