#Run this cell
import sys
# The following command points your notebook to the location of a folder outside your working directory that you want to import.
sys.path.append('./CreditCardKB_v2')
#sys.path.append('yourpath')
import driver_simple

driver_simple.bc_test()

driver_simple.bc_test_questions()