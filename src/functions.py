import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ', level=logging.INFO)


def args_2_para(args):
    """Documentation:
    inputs:
            args: arguments of argparser
    this function retrieves the parameters of the Argparser
    """
    logging.info('start getting parameters')
    file : str = args.input_file
    out_dir : str = args.output_dir
    overwrite : str = args.overwrite
    dry_run: bool = args.d

    return file, out_dir, overwrite, dry_run
