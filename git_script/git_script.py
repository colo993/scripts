import subprocess
import argparse

parser=argparse.ArgumentParser(description="Commit changes to selected branch")

parser.add_argument("files_name", help="Files to commit. For specific files use 'file1 file2 file3'. For all files use .")
parser.add_argument("commit_name", help="Your current commit name")
parser.add_argument("branch_name", help="Your branch name to pushed changes")

args=parser.parse_args()

files_name = args.files_name
commit_name = args.commit_name
branch_name = args.branch_name

subprocess.call(f"git add {files_name}", shell=True)
subprocess.call(f"git commit -m {commit_name}", shell=True)
subprocess.call(f"git push -u origin {branch_name}", shell=True)
