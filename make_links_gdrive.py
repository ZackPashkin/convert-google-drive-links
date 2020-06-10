import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=input, help='Enter your link path here like /home/user/links.txt',default='Enter link path here: ')
    args = parser.parse_args()
    sys.stdout.write(str(make_links_gdrive(args)))

def make_links_gdrive(args):
    edited_links_list=[]
    with open(os.path.join(os.getcwd(),args.path), 'r') as f:
        links = f.readlines()    
        for link in links:
            edited_links = link.split('/view')
            edited_links =edited_links[0].replace('file/d/', 'uc?id=')
            print(edited_links)
            edited_links = f"\n{edited_links}"
            edited_links_list.append(edited_links)
    with open(os.path.join(os.getcwd(),args.path), 'a') as f:
            f.writelines(edited_links_list)

if __name__ ==  '__main__':
    main()
    
    

    

