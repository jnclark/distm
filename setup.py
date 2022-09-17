from setuptools import setup
import os
import subprocess


def cmake_build_lib():
    os.makedirs('build', exist_ok=True)
    os.chdir('build')
    subprocess.run(["cmake", ".."])
    subprocess.run(["make"])
    os.chdir('..')
    subprocess.run(["mv", "build/lib/cpp/libdistm.so", "src/distm/libdistm.so"])


if __name__ == '__main__':
    cmake_build_lib()
    setup()
