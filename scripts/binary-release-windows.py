import subprocess
import os

uname = 'Windows'
branch = os.environ.get('GITHUB_REF').split('/')[-1]
commit = os.environ.get('GITHUB_SHA')

p = subprocess.run('cargo build -p near-vm-runner-standalone --release', shell=True)
assert p.returncode == 0
p = subprocess.run(f'aws s3 cp --acl public-read target/release/near-vm-runner-standalone s3://build.nearprotocol.com/nearcore/{uname}/{branch}/', shell=True)
assert p.returncode == 0
p = subprocess.run(f'aws s3 cp --acl public-read target/release/near-vm-runner-standalone s3://build.nearprotocol.com/nearcore/{uname}/{branch}/{commit}/', shell=True)
assert p.returncode == 0