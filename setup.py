from setuptools import setup, find_packages

setup(
    name='m4',
    version='0.1.0',
    description='A brief description of your project',
    author='Rahim Khan',
    author_email='rahim.khan@xelpmoc.in',
    url='https://github.com/rahim-xelpmoc/m4',
    packages=find_packages(),  # Automatically find and include all packages in your project
    install_requires=[
        'torch',
        'transformers'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
)
