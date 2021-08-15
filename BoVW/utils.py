import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Arguments for descriptos")
    tasks = parser.add_subparsers(title="subcommands", description="available tasks", dest="task", metavar="")

    sift = tasks.add_parser("sift",
                            help="Use sift Feature Detection")
    sift.add_argument("-i", "--input", required=True, help="Input Folder")
    sift.add_argument("-o", "--output", required=False, help="Output Folder")

    surf = tasks.add_parser("surf",
                            help="Use surf Feature Detection")
    surf.add_argument("-i", "--input", required=True, help="Input Folder")
    surf.add_argument("-o", "--output", required=False, help="Output Folder")

    orb = tasks.add_parser("orb",
                           help="Use orb Feature Detection")
    orb.add_argument("-i", "--input", required=True, help="Input Folder")
    orb.add_argument("-o", "--output", required=False, help="Output Folder")
    return
