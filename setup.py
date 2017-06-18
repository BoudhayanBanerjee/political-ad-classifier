from setuptools import setup, find_packages

setup(name="adclassifier",
      version="1.0",
      description="youtube political video classifier",
      author="Boudhayan Banerjee",
      author_email="bbanerji@iastate.edu",
      license='MIT',
      packages=find_packages(exclude=['test', 'test.*']),
      test_suite="test"
      )
