"""This is the __init__ file for the chapmanbe package"""

__all__ = ["my_favorite_functions", "hello"]
from . import my_favorite_functions
import getpass
import os
creator_name = "Brian Chapman"
your_name = getpass.getuser()

#try:
#    os.mkdir(os.path.join(os.path.expanduser("~"), ".chapmanbe_data"))
#except: FileExistsError
#    pass

if not os.path.exists(os.path.join(os.path.expanduser("~"), ".chapmanbe_data")):
                      os.mkdir(os.path.join(os.path.expanduser("~"), ".chapmanbe_data"))