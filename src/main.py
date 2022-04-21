import argparse
import __init__ as init
from pii import pii
from functions import args_2_para

# %% defined command line options for input_file name, this also generates --help and error handling
CLI = argparse.ArgumentParser()
CLI.add_argument(
    "--input_file",   # name on the CLI - drop the `--` for positional/required parameters
    # nargs="*",  # 0 or more values expected => creates a list
    type=str,
    required=True,
    default='',  # default if nothing is provided
    help='the file to be processed',
)

# %% defined command line options for output_dir name, this also generates --help and error handling
CLI.add_argument(
    "--output_dir",   # name on the CLI - drop the `--` for positional/required parameters
    # nargs="*",  # 0 or more values expected => creates a list
    type=str,
    default='',  # default if nothing is provided
    help='the path to results',
)

CLI.add_argument(
    '--overwrite',
    action="store_true",
    help='Bool type')


CLI.add_argument(
    '-v', '--version',
    action='version',
    version="%(prog)s (" + init.__version__ + ")")

CLI.add_argument(
    '-d', '--dry-run',
    help="bool, run the program in the dry mode",
    action="store_true")


args = CLI.parse_args()


file, out_dir, overwrite, dry_run, col_tolr, nb_mergrow, tresh_nan, prct_insign, save_dropped = args_2_para(args)
pii(file, out_dir, overwrite, dry_run)


# %%
