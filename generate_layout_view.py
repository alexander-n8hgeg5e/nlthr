#!/usr/bin/env python3
#
#    nlthr generate layout helper Copyright (C) 2017 Alexander Wilhelmi
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from shlex import split
import subprocess
pdftkcmd=['pdftk']
rmcmd=['rm']
subprocess.check_call(['xkbcomp','2.xkb'])
for i in [1,3,5,7]:
    cmd=split('xkbprint -color -level2 -ll '+str(i)+' 2.xkm keyboard_l'+str(i)+'.ps')
    subprocess.check_call(cmd)
    subprocess.check_call(['ps2pdf','keyboard_l'+str(i)+'.ps'])
    subprocess.check_call(['rm','keyboard_l'+str(i)+'.ps'])
    pdftkcmd.append('keyboard_l'+str(i)+'.pdf')
    rmcmd.append('keyboard_l'+str(i)+'.pdf')
pdftkcmd=pdftkcmd+['output','keyboardlayout.pdf']
rmcmd=rmcmd+['2.xkm']
subprocess.check_call(pdftkcmd)
subprocess.check_call(rmcmd)

        
 
