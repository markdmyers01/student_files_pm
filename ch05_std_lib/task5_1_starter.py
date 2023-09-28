"""

      task5_1_starter.py    -   Using os.walk()

      Create a script, using os.walk(), to find the two .jpg images
      hidden within the student_files.

      Make a copy of these files and place them into the
      student_files/resources/images folder.

      Warning!!!: If you try to copy files into the same directory,
                  you will get a SameFileError exception.  (We will walk the
                  resources/images directory and we are copying files into this
                  location also).
                  There are three ways around this:
                  1. Handle SameFileError exceptions (doing nothing in the except block)
                  2. Exclude the destination from being walked

      We'll use #2 above.



    Step 1. Begin calling os.walk() specify our root_directory to walk.

    Step 2. To avoid walking our destination directory (which happens to be WITHIN
            the student_files directory, we will check for it and avoid it):

                path = os.path.abspath(curdir)          # curdir is the first value back from os.walk() here
                if path != dstpath:                     # make sure it is different than dstpath


    Step 3. Iterate over the files at the current directory.  Check if they end with
            .jpg.


    Step 4. If it is a .jpg file, shutil.copy() it to the dstpath.  You should join
            the current directory and filename and then copy that filepath to the dstpath
            location.


    Step 5. Test it out!
"""
import os
import shutil

root_directory = '..'
dst = 'resources/images'
copied = 0
dstpath = os.path.abspath(os.path.join(root_directory, dst))

