# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'facts_yi.kfb'):
           [1649018298.71821, 'facts_yi.fbc'],
         ('', '', 'questions_yi.kqb'):
           [1649018298.737208, 'questions_yi.qbc'],
         ('', '', 'yi_rules.krb'):
           [1649018298.7482762, 'yi_rules_bc.py'],
         ('', '', 'yi_rules_questions.krb'):
           [1649018298.7599869, 'yi_rules_questions_bc.py'],
        },
        compiler_version)

