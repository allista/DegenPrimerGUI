# Copyright (C) 2012 Allis Tauri <allista@gmail.com>
# 
# indicator_gddccontrol is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# indicator_gddccontrol is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
Created on Jul 27, 2012

@author: Allis Tauri <allista@gmail.com>
'''

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from distutils.core import setup
setup(name='degen-primer-gui',
      version='1.0',
      description='Qt GUI for DegenPrimer',
      long_description=read('README'),
      license='GPL-3',
      author='Allis Tauri',
      author_email='allista@gmail.com',
      url='https://launchpad.net/degenprimergui',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX',
        'Programming Language :: Python'],
      packages=['DegenPrimerGUI'],
      scripts=['degen_primer_gui'],
      data_files=[('share/applications', ['DegenPrimerGUI.desktop'])
                  ('share/degen_primer', ['DegenPrimerUI.ui', 'ReportWidget.ui'])]
      )