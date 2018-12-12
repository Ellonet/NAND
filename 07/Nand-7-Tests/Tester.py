# Script by Kali
# V.1

import os.path
import subprocess
from os.path import join

# Do not change this
EXAMPLE_DIR = 'Examples7'

# TODO: SET THESE IF YOU WANT THE SCRIPT TO WORK PROPERLY!!!
# The relative path to the VM's main script.
MAIN_REL_PATH = r"C:\\Users\\Dell\\Desktop\\year2\\semester a\\nand\\ex1\\nand-ex1\\07\\ex07\\Main.py"
# The relative path to the CPU emulator executable.
CPU_EMU_REL_PATH = r"C:\Users\Dell\Desktop\year2\semester a\\nand\\nand2tetris\\nand2tetris\\tools\CPUEmulator.bat"
# Set to true if you'r using python3 command to run python.
PYTHON_3 = True


def run_single(example_name):
    # Get full paths out of relative paths
    example_dir_rel = join(EXAMPLE_DIR, example_name)
    if not os.path.isdir(example_dir_rel):
        return
    example_dir = os.path.abspath(example_dir_rel)
    vm_path = os.path.abspath(MAIN_REL_PATH)
    cpu_emu_path = os.path.abspath(CPU_EMU_REL_PATH)
    tst_path = join(example_dir, example_name + '.tst')
    python_cmd = "python" + ("3" if PYTHON_3 else "")

    print()

    print('Now translating example: ' + example_name)
    args = [python_cmd, vm_path, example_dir]
    subprocess.call(args)

    print('Running the test...')
    args = [cpu_emu_path, tst_path]
    subprocess.call(args)


names = os.listdir(EXAMPLE_DIR)
for test_dir in names:
    run_single(test_dir)

# run_single("BasicTest")
