import os as _os


def _set_credentials():
    try:
        home = _os.path.expanduser("~")
        with open(home + '/.pypi_umihico_env', 'r') as f:
            for line in f.readlines():
                key, password = line.split(',')
                _os.environ[key] = password.replace('\n', '')
    except Exception as e:
        pass


_set_credentials()


def _set_env_value(getenv_key, optional_value=None):
    """
    example
    def send_line(message, receiver_api_key=None):
        receiver_api_key = _set_env_value('line_api_key', receiver_api_key)
    """
    value = _os.getenv(getenv_key) or optional_value
    if not value:
        raise Exception(f"{getenv_key} is not defined")
    return value


if __name__ == '__main__':
    import api
    import scraping
    print([_os.environ['line_api_key'], ])
    api.line.send_line('test', receiver_api_key=None)
else:
    from . import api
    from . import scraping
