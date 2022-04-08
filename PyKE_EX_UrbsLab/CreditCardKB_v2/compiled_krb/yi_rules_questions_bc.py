# yi_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (2,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (1,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (3,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (3,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (1,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (3,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (2,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (3,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Aventura_Visa_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (2,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Aventura_Visa_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (1,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Costco_Mastercard(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Costco_Mastercard: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Costco_Mastercard: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Costco_Mastercard: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Costco_Mastercard: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Costco_Mastercard: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (1,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Costco_Mastercard: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (1,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Select_Visa_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Select_Visa_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Select_Visa_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Select_Visa_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Select_Visa_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Select_Visa_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (3,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Select_Visa_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (2,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (3,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (1,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (3,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (2,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (2,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (2,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (3,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (1,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (1,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (3,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (2,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (3,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (1,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'usage', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      with engine.prove('questions_yi', 'annual_income', context,
                                        (rule.pattern(2),)) \
                        as gen_5:
                        for x_5 in gen_5:
                          assert x_5 is None, \
                            "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege: got unexpected plan from when clause 5"
                          if context.lookup_data('ans') in (3,):
                            with engine.prove('questions_yi', 'benefits', context,
                                              (rule.pattern(2),)) \
                              as gen_7:
                              for x_7 in gen_7:
                                assert x_7 is None, \
                                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege: got unexpected plan from when clause 7"
                                if context.lookup_data('ans') in (2,):
                                  with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                    (rule.pattern(2),)) \
                                    as gen_9:
                                    for x_9 in gen_9:
                                      assert x_9 is None, \
                                        "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege: got unexpected plan from when clause 9"
                                      if context.lookup_data('ans') in (3,):
                                        rule.rule_base.num_bc_rule_successes += 1
                                        yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_TD_Rewards_Visa_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_TD_Rewards_Visa_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_TD_Rewards_Visa_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'benefits_student', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_TD_Rewards_Visa_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Aeroplan_Visa_Card_for_Students(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Card_for_Students: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Card_for_Students: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'benefits_student', context,
                                  (rule.pattern(1),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Aeroplan_Visa_Card_for_Students: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Dividend_Visa_Card_for_Students(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Dividend_Visa_Card_for_Students: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Dividend_Visa_Card_for_Students: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'benefits_student', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Dividend_Visa_Card_for_Students: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (2,):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_ScotiaBank_Scene_Card(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_ScotiaBank_Scene_Card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_ScotiaBank_Scene_Card: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'benefits_student', context,
                                  (rule.pattern(2),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_ScotiaBank_Scene_Card: got unexpected plan from when clause 3"
                    if context.lookup_data('ans') in (1,):
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_nothing(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove('questions_yi', 'is_citizen', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_credit_card_suit_you_nothing: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_nothing: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('yi_rules_questions')
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Card, None,
                  (pattern.pattern_literal('CIBC_Aeroplan_Visa_Infinite_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Aventura_Visa_Infinite_Privilege_Card, None,
                  (pattern.pattern_literal('CIBC_Aventura_Visa_Infinite_Privilege_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Aventura_Gold_Visa_Card, None,
                  (pattern.pattern_literal('CIBC_Aventura_Gold_Visa_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Aventura_Visa_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Aventura_Visa_Card, None,
                  (pattern.pattern_literal('CIBC_Aventura_Visa_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Costco_Mastercard', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Costco_Mastercard, None,
                  (pattern.pattern_literal('CIBC_Costco_Mastercard'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Select_Visa_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Select_Visa_Card, None,
                  (pattern.pattern_literal('CIBC_Select_Visa_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_bizline_Visa_Card_for_Business, None,
                  (pattern.pattern_literal('CIBC_bizline_Visa_Card_for_Business'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_TD_Emerald_Flex_Rate_Visa_Card, None,
                  (pattern.pattern_literal('TD_Emerald_Flex_Rate_Visa_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_TD_Cash_Back_Visa_Infinite_Card, None,
                  (pattern.pattern_literal('TD_Cash_Back_Visa_Infinite_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_TD_Aeroplan_Visa_Business_Card, None,
                  (pattern.pattern_literal('TD_Aeroplan_Visa_Business_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_TD_Business_Select_RateTM_Visa_Card, None,
                  (pattern.pattern_literal('TD_Business_Select_RateTM_Visa_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Aeroplan_Visa_Infinite_Privilege, None,
                  (pattern.pattern_literal('CIBC_Aeroplan_Visa_Infinite_Privilege'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_TD_Rewards_Visa_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_TD_Rewards_Visa_Card, None,
                  (pattern.pattern_literal('TD_Rewards_Visa_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Aeroplan_Visa_Card_for_Students', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Aeroplan_Visa_Card_for_Students, None,
                  (pattern.pattern_literal('CIBC_Aeroplan_Visa_Card_for_Students'),),
                  (),
                  (pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Dividend_Visa_Card_for_Students', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Dividend_Visa_Card_for_Students, None,
                  (pattern.pattern_literal('CIBC_Dividend_Visa_Card_for_Students'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_ScotiaBank_Scene_Card', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_ScotiaBank_Scene_Card, None,
                  (pattern.pattern_literal('ScotiaBank_Scene_Card'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_nothing', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_nothing, None,
                  (pattern.pattern_literal('Sorry_nothing_fits_you'),),
                  (),
                  (pattern.pattern_literal(False),))


Krb_filename = '..\\yi_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (6, 6)),
    ((20, 25), (8, 8)),
    ((26, 31), (9, 9)),
    ((32, 37), (10, 10)),
    ((38, 38), (11, 11)),
    ((39, 44), (12, 12)),
    ((45, 45), (13, 13)),
    ((46, 51), (14, 14)),
    ((52, 52), (15, 15)),
    ((53, 58), (16, 16)),
    ((59, 59), (17, 17)),
    ((72, 76), (21, 21)),
    ((78, 83), (23, 23)),
    ((84, 89), (24, 24)),
    ((90, 95), (25, 25)),
    ((96, 96), (26, 26)),
    ((97, 102), (27, 27)),
    ((103, 103), (28, 28)),
    ((104, 109), (29, 29)),
    ((110, 110), (30, 30)),
    ((111, 116), (31, 31)),
    ((117, 117), (32, 32)),
    ((130, 134), (36, 36)),
    ((136, 141), (38, 38)),
    ((142, 147), (39, 39)),
    ((148, 153), (40, 40)),
    ((154, 154), (41, 41)),
    ((155, 160), (42, 42)),
    ((161, 161), (43, 43)),
    ((162, 167), (44, 44)),
    ((168, 168), (45, 45)),
    ((169, 174), (46, 46)),
    ((175, 175), (47, 47)),
    ((188, 192), (51, 51)),
    ((194, 199), (53, 53)),
    ((200, 205), (54, 54)),
    ((206, 211), (55, 55)),
    ((212, 212), (56, 56)),
    ((213, 218), (57, 57)),
    ((219, 219), (58, 58)),
    ((220, 225), (59, 59)),
    ((226, 226), (60, 60)),
    ((227, 232), (61, 61)),
    ((233, 233), (62, 62)),
    ((246, 250), (66, 66)),
    ((252, 257), (68, 68)),
    ((258, 263), (69, 69)),
    ((264, 269), (70, 70)),
    ((270, 270), (71, 71)),
    ((271, 276), (72, 72)),
    ((277, 277), (73, 73)),
    ((278, 283), (74, 74)),
    ((284, 284), (75, 75)),
    ((285, 290), (76, 76)),
    ((291, 291), (77, 77)),
    ((304, 308), (81, 81)),
    ((310, 315), (83, 83)),
    ((316, 321), (84, 84)),
    ((322, 327), (85, 85)),
    ((328, 328), (86, 86)),
    ((329, 334), (87, 87)),
    ((335, 335), (88, 88)),
    ((336, 341), (89, 89)),
    ((342, 342), (90, 90)),
    ((343, 348), (91, 91)),
    ((349, 349), (92, 92)),
    ((362, 366), (96, 96)),
    ((368, 373), (98, 98)),
    ((374, 379), (99, 99)),
    ((380, 385), (100, 100)),
    ((386, 386), (101, 101)),
    ((387, 392), (102, 102)),
    ((393, 393), (103, 103)),
    ((394, 399), (104, 104)),
    ((400, 400), (105, 105)),
    ((401, 406), (106, 106)),
    ((407, 407), (107, 107)),
    ((420, 424), (111, 111)),
    ((426, 431), (113, 113)),
    ((432, 437), (114, 114)),
    ((438, 443), (115, 115)),
    ((444, 444), (116, 116)),
    ((445, 450), (117, 117)),
    ((451, 451), (118, 118)),
    ((452, 457), (119, 119)),
    ((458, 458), (120, 120)),
    ((459, 464), (121, 121)),
    ((465, 465), (122, 122)),
    ((478, 482), (126, 126)),
    ((484, 489), (128, 128)),
    ((490, 495), (129, 129)),
    ((496, 501), (130, 130)),
    ((502, 502), (131, 131)),
    ((503, 508), (132, 132)),
    ((509, 509), (133, 133)),
    ((510, 515), (134, 134)),
    ((516, 516), (135, 135)),
    ((517, 522), (136, 136)),
    ((523, 523), (137, 137)),
    ((536, 540), (141, 141)),
    ((542, 547), (143, 143)),
    ((548, 553), (144, 144)),
    ((554, 559), (145, 145)),
    ((560, 560), (146, 146)),
    ((561, 566), (147, 147)),
    ((567, 567), (148, 148)),
    ((568, 573), (149, 149)),
    ((574, 574), (150, 150)),
    ((575, 580), (151, 151)),
    ((581, 581), (152, 152)),
    ((594, 598), (156, 156)),
    ((600, 605), (158, 158)),
    ((606, 611), (159, 159)),
    ((612, 617), (160, 160)),
    ((618, 618), (161, 161)),
    ((619, 624), (162, 162)),
    ((625, 625), (163, 163)),
    ((626, 631), (164, 164)),
    ((632, 632), (165, 165)),
    ((633, 638), (166, 166)),
    ((639, 639), (167, 167)),
    ((652, 656), (171, 171)),
    ((658, 663), (173, 173)),
    ((664, 669), (174, 174)),
    ((670, 675), (175, 175)),
    ((676, 676), (176, 176)),
    ((677, 682), (177, 177)),
    ((683, 683), (178, 178)),
    ((684, 689), (179, 179)),
    ((690, 690), (180, 180)),
    ((691, 696), (181, 181)),
    ((697, 697), (182, 182)),
    ((710, 714), (187, 187)),
    ((716, 721), (189, 189)),
    ((722, 727), (190, 190)),
    ((728, 733), (191, 191)),
    ((734, 734), (192, 192)),
    ((747, 751), (196, 196)),
    ((753, 758), (198, 198)),
    ((759, 764), (199, 199)),
    ((765, 770), (200, 200)),
    ((771, 771), (201, 201)),
    ((784, 788), (205, 205)),
    ((790, 795), (207, 207)),
    ((796, 801), (208, 208)),
    ((802, 807), (209, 209)),
    ((808, 808), (210, 210)),
    ((821, 825), (214, 214)),
    ((827, 832), (216, 216)),
    ((833, 838), (217, 217)),
    ((839, 844), (218, 218)),
    ((845, 845), (219, 219)),
    ((858, 862), (224, 224)),
    ((864, 869), (226, 226)),
    ((870, 875), (227, 227)),
)
