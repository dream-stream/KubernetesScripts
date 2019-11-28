#pip install paramiko

#   sudo apt-get update && sudo apt-get install nfs-common -y
#   sudo sed -i '27iswapoff\ -a' /etc/rc.local

from paramiko import SSHClient
import argparse

parser = argparse.ArgumentParser(description='Command to execute')
parser.add_argument('Command', metavar='Cmd', type=str, help='Command to execute')
args = parser.parse_args()

def main():
    sshClient = SSHClient()
    sshClient.load_system_host_keys()
    global args

    for rpi in range(1,9):
        print(f'Connecting to rpi{rpi}')

        sshClient.connect(f'worker{rpi}', username='pi', password='raspberry')
        print('Executing: ' + args.Command)
        _, stdout, _ = sshClient.exec_command(args.Command)

        for line in stdout:
            print(f'rpi{rpi}: ' + line.strip('\n'))

    print(f'Connecting to Master')
    sshClient.connect(f'master', username='pi', password='raspberry')
    print('Executing: ' + args.Command)
    _, stdout, _ = sshClient.exec_command(args.Command)
    
    for line in stdout:
        print(f'Master: ' + line.strip('\n'))

    sshClient.close()  

if __name__ == "__main__":
    main()