###################################################################################################
# This script returns a short string describing the major version of python being used.
#
# While it should be versatile, it was written with the intention that it will help resolve which
# requirements.txt to pull concrete-dependencies from.
###################################################################################################
import sys

print('py{}'.format(sys.version_info[0]))
