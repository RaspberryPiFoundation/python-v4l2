from setuptools import setup

setup(
    name='v4l2-python3',
    version='0.3.1',
    license='GPLv2',
    requires=('ctypes',),
    py_modules=('v4l2',),

    maintainer='Raspberry Pi Foundation',
    maintainer_email='web@raspberrypi.org',
    url='https://pypi.org/project/v4l2-python3/',
    keywords='v4l2 video4linux video4linux2 binding ctypes',
    description='Python bindings for the v4l2 userspace api.',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Capture',
    ],
)
