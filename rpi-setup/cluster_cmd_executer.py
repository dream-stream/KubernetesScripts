#pip install paramiko

#   sudo apt-get update && sudo apt-get install nfs-common -y
#   sudo sed -i '27iswapoff\ -a' /etc/rc.local

from paramiko import SSHClient
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('command', metavar='cmd', type=str, help='Command to execute')

parser.add_argument('-m', '--master', action='store_true', dest='master', help='Include master node in the execution')
parser.add_argument('-d', '--debian', action='store_true', dest='debian', help='Include debian node in the execution')
parser.add_argument('-a', '--all', action='store_true', dest='all', help='Include all nodes in the execution')

args = parser.parse_args()

def main():
    sshClient = SSHClient()
    sshClient.load_system_host_keys()
    global args

    for rpi in range(1,9):
        print(f'Connecting to Worker{rpi}')

        sshClient.connect(f'worker{rpi}', username='pi', password='raspberry')
        print('Executing: ' + args.command)
        _, stdout, _ = sshClient.exec_command(args.command)

        for line in stdout:
            print(f'Worker{rpi}: ' + line.strip('\n'))

        print("")


    if args.master or args.all:
        print(f'Connecting to Master')
        sshClient.connect(f'master', username='pi', password='raspberry')
        print('Executing: ' + args.command)
        _, stdout, _ = sshClient.exec_command(args.command)
    
        for line in stdout:
            print(f'Master: ' + line.strip('\n'))
        
        print("")

    if args.debian or args.all:
        print(f'Connecting to Debian')
        sshClient.connect(f'debian', username='nicklas', password='raspberry')
        print('Executing: ' + args.command)
        _, stdout, _ = sshClient.exec_command(args.command)
    
        for line in stdout:
            print(f'Debian: ' + line.strip('\n'))

    sshClient.close()  

if __name__ == "__main__":
    main()