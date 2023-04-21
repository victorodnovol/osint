from distutils.core import setup

setup(name='osint',
      version='1.0',
      description='OSINT module',
      author='Viktor',
      author_email='viktor.odnovol@gmail.com',
      packages=['full_scripts', ''],
      package_dir={
          'full_scripts': 'full_scripts',
          '': '.'
      },
      package_data={'full_scripts': ['*.dat', '*.txt']},
      entry_points={
          'console_scripts': [
              'osint = frame:cli',
          ],
      })
