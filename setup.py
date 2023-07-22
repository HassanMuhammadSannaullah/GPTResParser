from setuptools import setup, find_packages

setup(
    name='GPTResParser',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pdfminer.six',
        'python-docx',
        'regex',
        'aiohttp',
        'freeGPT==1.1.2',
        'docx2txt==0.8'
    ],
    # Include any other relevant metadata
    author='Hassan Muhammad Sanaullah',
    description='A GPT3 based resume extractor for quick and light weight extraction from Resumes',
    url='https://github.com/HassanMuhammadSannaullah/GPTResParser',
)
