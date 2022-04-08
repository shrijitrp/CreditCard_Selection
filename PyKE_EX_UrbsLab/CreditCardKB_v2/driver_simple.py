import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)

# to run the expert system
def bc_test():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('yi_rules') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")
    
    try:
        with engine.prove_goal('yi_rules.what_to_bring($bring)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("You should bring: %s" % (vars['bring'])) #STUDENTS: you will need to edit this line
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
    # engine.print_stats()

    
def bc_test_questions():

    engine.reset()      # Allows us to run tests multiple times.

    engine.activate('yi_rules_questions') #STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")
    
    try:
        with engine.prove_goal('yi_rules_questions.what_credit_card_suit_you($bring)') as gen: #STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("The credit card suit you the best is: %s" % (vars['bring'])) #STUDENTS: you will need to edit this line
                # print("link: %s" % (vars['link'])) #STUDENTS: you will need to edit this line

    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")


