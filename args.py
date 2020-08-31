""" Bag of Visual Wordsgit"""
import argparse
import os

def sift():
    pass

def surf():
    pass

def orb():
    pass





def parse_arguments():
    '''
    Command Line Argument Parser
    '''
    parser = argparse.ArgumentParser(description= "Arguments for descriptos")
    tasks = parser.add_subparsers(title= "subcommands", description= "available tasks", dest= "task", metavar= "")

    sift = tasks.add_parser("sift",
                            help = "Use sift Feature Detection")
    sift.add_argument("-i", "--input", required= True, help= "Input Folder")
    sift.add_argument("-o", "--output", required= False, help= "Output Folder")

    surf = tasks.add_parser("surf",
                            help = "Use surf Feature Detection")
    surf.add_argument("-i", "--input", required= True, help= "Input Folder")
    surf.add_argument("-o", "--output", required= False, help= "Output Folder")
    
    orb = tasks.add_parser("orb",
                            help = "Use orb Feature Detection")
    orb.add_argument("-i", "--input", required= True, help= "Input Folder")
    orb.add_argument("-o", "--output", required= False, help= "Output Folder")
    return

if __name__ == "__main__":
    """ Main Program """

    args = parse_arguments()

    if args.tasks == "sift":
        print("sift")
    elif args.tasks == "surf":
        print("surf")
    elif args.tasks == "orb":
        print("orb")
    else :
        raise "Invalid feature extractor, Try again"
    exit(0)