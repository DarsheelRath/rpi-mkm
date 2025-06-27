from setuptools import setup, find_packages 
setup( name="rpi-mkm",
      version="1.0.0",
      description="A brief description of your package",
      author="Darsheel Rath",
      author_email="darsheelrath@gmail.com",
      packages=find_packages(),
      install_requires=[ # List your dependencies here ],
      classifiers=[ 'Development Status :: 3 - Alpha', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.11', ], )
