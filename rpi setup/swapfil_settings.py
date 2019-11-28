#Disable Swapfile on RPI

#pip install paramiko

from paramiko import SSHClient

def main():
    sshClient = SSHClient()
    sshClient.load_system_host_keys()
    
    for rpi in range(1,9):
        print(f'Connecting to Worker{rpi}')

        sshClient.connect(f'worker{rpi}', username='pi', password='raspberry')
        _, stdout, _ = sshClient.exec_command(r"sudo sed -i '27iswapoff\ -a' /etc/rc.local")

        for line in stdout:
            print(f'rpi{rpi}: ' + line.strip('\n'))

    sshClient.connect(f'master', username='pi', password='raspberry')
    _, stdout, _ = sshClient.exec_command(r"sudo sed -i '27iswapoff\ -a' /etc/rc.local")
    for line in stdout:
        print(f'Master: ' + line.strip('\n'))

    sshClient.close()  

if __name__ == "__main__":
    main()