import os as _os


def _set_credentials():
    try:
        home = _os.path.expanduser("~")
        with open(home + '/.pypi_umihico_env', 'r') as f:
            for line in f.readlines():
                key, password = line.split(':')
                key = 'umihico_' + key
                _os.environ[key] = password.replace('\n', '')
    except Exception as e:
        pass


_set_credentials()

if __name__ == '__main__':
    import api
    import scraping
    print([_os.environ['umihico_line_api_key'], ])
    api.line.send_line('test', receiver_api_key=None)
else:
    from . import api
    from . import scraping
