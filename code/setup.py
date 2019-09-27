#!/usr/bin/env python

# from distutils.core import setup

# setup(
    # name='demolib',
    # version='0.1',
    # description='Demolib',
    # author='Linden Lab',
    # author_email='not.your@business.com',
    # url='https://github.com/vancun/demofraud/tree/master/code/demolib',
    # packages=['demolib'])


import os
import shutil
from setuptools import setup


OUTPUT_DIR = '../lib'


if __name__ == "__main__":
    setup(
        name="demolib",
        packages=['demolib'],
        version="1.0",
        script_args=['--quiet', 'bdist_egg'], # to create egg-file only
    )

    egg_name = os.listdir('dist')[0]
    
    if os.path.isfile(os.path.join(OUTPUT_DIR, egg_name)):
        os.remove(os.path.join(OUTPUT_DIR, egg_name))
    
    os.rename(
        os.path.join('dist', egg_name),
        os.path.join(OUTPUT_DIR, egg_name)
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('demolib.egg-info')
    