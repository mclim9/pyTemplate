"""Project Command Line Interface"""
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description='Project Helper')
    parser.add_argument('-f','--foo', required=False, help='You want to Foo')
    parser.add_argument('-b','--bar', required=False, help='You want to Bar')
    args = parser.parse_args()          #Dictionary of args

    print(f'Examples@ {os.path.dirname(__file__)}\\examples')
    os.chdir(os.path.dirname(__file__)+'\\examples')

    if args.foo:
        try:
            print(f'Foo is: {args.foo}')
        except:
            pass

    if args.bar:
        print(f'Bar is: {args.bar}')

    # print(f'Number of arguments: {len(sys.argv)} arguments.')
    # print(f'Argument List:{str(sys.argv)}')

if __name__ == "__main__":
    print(os.path.dirname(__file__))
    main()
    sys.exit(0)
