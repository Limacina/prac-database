from argparse import ArgumentParser

def parse():
    parser = ArgumentParser(description='Database connection')
    parser.add_argument(
        '--database',
        type=str,
        help='path to a FDB database'
    )
    parser.add_argument(
        '--user',
        type=str,
        help='username to access the database'
    )
    parser.add_argument(
        '--password',
        type=str,
        help='password to access the database'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=60,
        help='observation interval in minutes. Default value equals to 60 (one hour)'
    )
    parser.add_argument(
        '--start',
        type=str,
        help='time in format "hh:mm:ss" to start the program'
    )

    return parser.parse_args()
