#Run this cell
import sys
# The following command points your notebook to the location of a folder outside your working directory that you want to import.
sys.path.append('./simple_bc_all')
#sys.path.append('yourpath')
import driver_simple

driver_simple.bc_test()

driver_simple.bc_test_questions()