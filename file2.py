import os

from paramiko import Transport, SFTPClient


def remote_scp(ftp_type, host_ip, remote_path, local_path, username, password):
    ssh_port = 22
    try:
        conn = Transport((host_ip, ssh_port))
        conn.connect(username=username, password=password)
        sftp = SFTPClient.from_transport(conn)
        if ftp_type == 'remoteRead':
            print('read')
            if not local_path:
                filename = os.path.split(remote_path)
                local_path = os.path.join('/tmp', filename[-1])
            print('开始从服务器下载文件......')
            sftp.get(remote_path, local_path)
            print(f'文件{filename[-1]}已经下载到本地')

        if ftp_type == "remoteWrite":
            print('write')
            sftp.put(local_path, remote_path)

        conn.close()
        return True
    except IOError as e:
        print('没有找到目录', e)
    except Exception as e:
        print('error!!!', e)


remote_scp('remoteRead', '172.25.16.89', '/usr/local/aquila_pd_test/tomcat/dt.sh', '', 'aquila_pd_test', 'aquila_pd_test')
remote_scp('remoteWrite', '172.25.16.89', '/tmp/dt.sh', '/tmp/dt.sh', 'aquila_pd_test', 'aquila_pd_test')
