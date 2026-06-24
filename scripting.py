import sys
#  Argument variable - Pass in Argumenth
# arg1 = sys.argv
# print(arg1)

# Which File is being run:
# args = sys.argv
# print("Name of thr Script being run ", args[0])

# if len(sys.argv) > 1:
#     print(len(sys.argv) -1, 'arguments provided')
# else:
#     print("No Arguments")

# args = sys.argv
# name = sys.argv[1]
# print(f"Hello {name}")



# args = sys.argv

# if len(args) > 2:
#     result = int(args[1]) + int(args[2])
#     print(result)
# else:
#     print("Please provide 2 numbers")


# items = os.listdir()
# print(items)



# if len(sys.argv) > 1:
#     folder = sys.argv[1]

#     full_dir = os.listdir(folder)

#     for filename in full_dir:
#         if filename.endswith('.py'):
#             print(filename)
# else:
#     print("Please provide a folder path")

import subprocess
import subprocess
import sys
import pathlib
import os



# if len(sys.argv) < 2:
#     print("Please provide a folder path")
#     exit()

# path_to_dir = sys.argv[1]

# subprocess.run(["ls", "-a", path_to_dir])

# print(os.path.abspath("test_stone.py"))

import os

newdir = "test_dir"

current_dir = os.path.abspath('.')

newdir_location = os.path.join(current_dir, newdir)

# os.mkdir(newdir_location,)

# if os.path.exists(newdir_location):
#     newdir_location += "1"

# print("Directory created:", newdir_location)

try: 
    os.mkdir(newdir_location)
    print("Directory Created ", newdir_location)
except FileExistsError:
    print("Theres an error")
