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
         ('', '', 'bc_simple_rules.krb'):
           [1648488394.878, 'bc_simple_rules_bc.py'],
         ('', '', 'bc_simple_rules_questions.krb'):
           [1648488394.9124064, 'bc_simple_rules_questions_bc.py'],
         ('', '', 'facts.kfb'):
           [1648488394.9195013, 'facts.fbc'],
         ('', '', 'questions.kqb'):
           [1648488394.9772208, 'questions.qbc'],
        },
        compiler_version)

