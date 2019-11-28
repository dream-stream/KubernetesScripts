#Install of nfs-common on rpi cluster

#pip install paramiko

from paramiko import SSHClient

def main():
    sshClient = SSHClient()
    sshClient.load_system_host_keys()
    
    for rpi in range(1,9):
        print(f'Connecting to rpi{rpi}')

        sshClient.connect(f'worker{rpi}', username='pi', password='raspberry')
        _, stdout, _ = sshClient.exec_command('sudo apt-get update && sudo apt-get install nfs-common -y')

        for line in stdout:
            print(f'rpi{rpi}: ' + line.strip('\n'))

    sshClient.close()  

if __name__ == "__main__":
    main()