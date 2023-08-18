"""
Python Beyond The Basics: The Factory Pattern: DYNAMIC TYPE
"""
import abc


class ImageReader(metaclass=abc.ABCMeta):
    def __init__(self, path):
        self.path = path

    @abc.abstractmethod
    def read(self):
        print('ImageReader(metaclass=abc.ABCMeta):->')
        pass  # Subclass must implement.

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.path)


class GIFReader(ImageReader):
    def read(self):
        print('GIFReader(ImageReader):->')
        pass


class JPEGReader(ImageReader):
    def read(self):
        print('JPEGReader(ImageReader):->')
        pass

class PNGReader(ImageReader):
    def read(self):
        print('PNGReader(ImageReader):->')
        pass

class RawReader(ImageReader):
    def read(self):
        print('RawReader(ImageReader):->')
        pass

def extension_of(path_str):
    position_of_last_dot = path_str.rfind('.')
    return path_str[position_of_last_dot + 1:]


def get_image_reader(path):
    image_type = extension_of(path)
    reader_class = None
    if image_type == 'gif':
        reader_class = GIFReader
    elif image_type == 'jpg':
        reader_class = JPEGReader
    elif image_type == 'png':
        reader_class = PNGReader
    assert reader_class is not None, 'Unknown extension: {}'.format(image_type)
    return reader_class(path)


READERS = {
    'gif': GIFReader,
    'jpg': JPEGReader,
    'png': PNGReader,
}


def get_image_reader(path):
    try:
        reader_class = READERS[extension_of(path)]
    except KeyError:
        reader_class = RawByteReader
    return reader_class(path)


if __name__ == '__main__':
    print('The Factory Pattern: DYNAMIC TYPE')
    path_extension = extension_of('filename.gif')
    print(f'path_extension-->{path_extension}')
    path_extension = extension_of('filename.jpg')
    print(f'path_extension-->{path_extension}')
    path_extension = extension_of('filename.png')
    print(f'path_extension-->{path_extension}')

    obj_01 = get_image_reader('filename.gif')
    obj_02 = get_image_reader('filename.jpg')
    obj_03 = get_image_reader('filename.png')