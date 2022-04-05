# yi_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def what_credit_card_suit_you_CIBC_Visa_Infinite(rule, arg_patterns, arg_context):
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
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 2"
                with engine.prove('questions_yi', 'is_personal_use', context,
                                  (rule.pattern(0),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 3"
                    with engine.prove('questions_yi', 'is_business_use', context,
                                      (rule.pattern(1),)) \
                      as gen_4:
                      for x_4 in gen_4:
                        assert x_4 is None, \
                          "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 4"
                        with engine.prove('questions_yi', 'annual_income', context,
                                          (rule.pattern(2),)) \
                          as gen_5:
                          for x_5 in gen_5:
                            assert x_5 is None, \
                              "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 5"
                            if context.lookup_data('ans') in (1,):
                              with engine.prove('questions_yi', 'benefits', context,
                                                (rule.pattern(2),)) \
                                as gen_7:
                                for x_7 in gen_7:
                                  assert x_7 is None, \
                                    "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 7"
                                  if context.lookup_data('ans') in (1,):
                                    with engine.prove('questions_yi', 'expected_annual_fee', context,
                                                      (rule.pattern(2),)) \
                                      as gen_9:
                                      for x_9 in gen_9:
                                        assert x_9 is None, \
                                          "yi_rules_questions.what_credit_card_suit_you_CIBC_Visa_Infinite: got unexpected plan from when clause 9"
                                        if context.lookup_data('ans') in (1,):
                                          rule.rule_base.num_bc_rule_successes += 1
                                          yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_credit_card_suit_you_CIBC_Master_Infinite(rule, arg_patterns, arg_context):
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
              "yi_rules_questions.what_credit_card_suit_you_CIBC_Master_Infinite: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_student', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_credit_card_suit_you_CIBC_Master_Infinite: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('yi_rules_questions')
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Visa_Infinite', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Visa_Infinite, None,
                  (pattern.pattern_literal('CIBC_Aventura_Visa_Infinite_Card'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),
                   contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_credit_card_suit_you_CIBC_Master_Infinite', This_rule_base, 'what_credit_card_suit_you',
                  what_credit_card_suit_you_CIBC_Master_Infinite, None,
                  (pattern.pattern_literal('CIBI_Aventura_Master_Infinite_Card'),),
                  (),
                  (pattern.pattern_literal(False),
                   pattern.pattern_literal(True),))


Krb_filename = '..\\yi_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((26, 31), (7, 7)),
    ((32, 37), (8, 8)),
    ((38, 43), (9, 9)),
    ((44, 49), (10, 10)),
    ((50, 50), (11, 11)),
    ((51, 56), (12, 12)),
    ((57, 57), (13, 13)),
    ((58, 63), (14, 14)),
    ((64, 64), (15, 15)),
    ((77, 81), (18, 18)),
    ((83, 88), (20, 20)),
    ((89, 94), (21, 21)),
)
