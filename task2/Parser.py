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
        '--itemid',
        type=str,
        help='item id to check the values'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='output path'
    )

    return parser.parse_args()