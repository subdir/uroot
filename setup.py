from distutils.core import setup

if __name__ == '__main__':
    setup(
        name = 'uroot',
        version = '0.0.1',
        description = 'Simple sandboxing without superuser privileges',
        author = 'Alexey Akimov',
        author_email = 'subdir@gmail.com',
        url = 'https://github.com/subdir/uroot',
        scripts = [
            'uroot',
        ]
    )

