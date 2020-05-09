import read_files
import text_cleaner
import argparse

def main():
    
    parser = argparse.ArgumentParser(description='Process text files', prefix_chars='-')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-infile', nargs='?')

    group.add_argument('-infolder',
                    help='folder with filenames to get processed')

    parser.add_argument('-ex_stop', nargs='?', const=True, default=False, type=bool)
    parser.add_argument('-pun', nargs='?', const=True, default=False, type=bool) 
    parser.add_argument('-dig', nargs='?', const=True, default=False, type=bool)
    parser.add_argument('-lowc', nargs='?', const=True, default=False, type=bool) 
    
    args = parser.parse_args()
    args.pun
    args.dig
    args.ex_stop
    args.lowc
    args.infile
    args.infolder

    if args.infile:
        main_path = read_files.file_loader_single(args.infile)[1]
        text_cleaner.main_logic(main_path, args.ex_stop, args.pun, args.dig, args.lowc)
    else:
        main_path = read_files.file_loader_dir(args.infolder)[1]
        text_cleaner.main_logic(main_path, args.ex_stop, args.pun, args.dig, args.lowc)  

if __name__ == "__main__":
    print('Starting processing the files with given parameters')
    try:
        main()
        print('Process completed')
    except:
        print('Error occured, check your parameters!')
