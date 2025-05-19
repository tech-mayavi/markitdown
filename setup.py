from setuptools import setup, find_packages

setup(
    name='markitdown',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here if needed, e.g.:
        # 'openai-whisper',
        # 'torch',
    ],
    author='tech-mayavi',
    description='A modified version of Markitdown with Whisper support for audio',
    url='https://github.com/tech-mayavi/markitdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
