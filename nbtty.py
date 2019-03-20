
import os
import json


NGROK_URL = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'
GOTTY_URL = 'https://github.com/yudai/gotty/releases/download/v1.0.1/gotty_linux_amd64.tar.gz'


def run(cmd, daemon=False, split=True):
    if daemon:
        return get_ipython().system_raw(cmd + ' &')
    return get_ipython().getoutput(cmd, split=split)


class TTY(object):
    base_dir = '/tmp/jupyter-tty'
    gotty_port = 18080

    def install(self):
        base_dir = self.base_dir
        run(f'mkdir -p {base_dir}')
        ngrok_zip = os.path.join(base_dir, 'ngrok-stable-linux-amd64.zip')
        ngrok_bin = os.path.join(base_dir, 'ngrok')
        if not os.path.exists(ngrok_zip):
            run(f'wget {NGROK_URL} -P {base_dir}')
        if not os.path.exists(ngrok_bin):
            run(f'unzip {ngrok_zip} -d {base_dir}')

        gotty_zip = os.path.join(base_dir, 'gotty_linux_amd64.tar.gz')
        gotty_bin = os.path.join(base_dir, 'gotty')
        if not os.path.exists(gotty_zip):
            run(f'wget {GOTTY_URL} -P {base_dir}')
        if not os.path.exists(gotty_bin):
            run(f'tar xvf {gotty_zip} -C {base_dir}')


    def start(self):
        base_dir = self.base_dir
        port = self.gotty_port
        self.install()
        self.stop()
        gotty_bin = os.path.join(base_dir, 'gotty')
        run(f'{gotty_bin} -p {port} -w bash', daemon=True)
        ngrok_bin = os.path.join(base_dir, 'ngrok')
        run(f'{ngrok_bin} http {port}', daemon=True)

        res = run('curl -s http://localhost:4040/api/tunnels', split=False)
        public_url = json.loads(res.s)['tunnels'][0]['public_url']
        print(public_url)

    def stop(self):
        run('pkill ngrok')
        run('pkill gotty')
