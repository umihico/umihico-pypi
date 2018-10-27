import zlib as _zlib
import base64 as _base64


def decompress_text(compressed_text):
    return _zlib.decompress(_base64.b64decode(compressed_text)).decode()


def compress_text(text):
    compressed_text = _base64.b64encode(
        _zlib.compress(text.encode(), 9)).decode()
    return compressed_text


if __name__ == '__main__':
    longtext = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    compressed_text = compress_text(longtext)
    text = decompress_text(compressed_text)
    print(len(longtext), longtext)
    print(len(compressed_text), compressed_text)
    print(len(text), text)
    assert text == longtext
