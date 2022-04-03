# yi_rules_questions_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def no_buying(rule, arg_patterns, arg_context):
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
        with engine.prove('questions_yi', 'is_food', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.no_buying: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_america_express(rule, arg_patterns, arg_context):
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
        with engine.prove('questions_yi', 'is_food', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_to_bring_america_express: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_gas', context,
                              (rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_to_bring_america_express: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_master_card(rule, arg_patterns, arg_context):
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
        with engine.prove('questions_yi', 'is_food', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_to_bring_master_card: got unexpected plan from when clause 1"
            with engine.prove('questions_yi', 'is_gas', context,
                              (rule.pattern(0),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "yi_rules_questions.what_to_bring_master_card: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_phone(rule, arg_patterns, arg_context):
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
        with engine.prove('questions_yi', 'any_places', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_to_bring_phone: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (1,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_cash(rule, arg_patterns, arg_context):
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
        with engine.prove('questions_yi', 'any_places', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_to_bring_cash: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (2,3):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def what_to_bring_water(rule, arg_patterns, arg_context):
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
        with engine.prove('questions_yi', 'any_places', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "yi_rules_questions.what_to_bring_water: got unexpected plan from when clause 1"
            if context.lookup_data('ans') in (4,):
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('yi_rules_questions')
  
  bc_rule.bc_rule('no_buying', This_rule_base, 'what_to_bring',
                  no_buying, None,
                  (pattern.pattern_literal('presto_card'),),
                  (),
                  (pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_america_express', This_rule_base, 'what_to_bring',
                  what_to_bring_america_express, None,
                  (pattern.pattern_literal('america_express'),),
                  (),
                  (pattern.pattern_literal(True),
                   pattern.pattern_literal(False),))
  
  bc_rule.bc_rule('what_to_bring_master_card', This_rule_base, 'what_to_bring',
                  what_to_bring_master_card, None,
                  (pattern.pattern_literal('master_card'),),
                  (),
                  (pattern.pattern_literal(True),))
  
  bc_rule.bc_rule('what_to_bring_phone', This_rule_base, 'what_to_bring',
                  what_to_bring_phone, None,
                  (pattern.pattern_literal('phone'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_bring_cash', This_rule_base, 'what_to_bring',
                  what_to_bring_cash, None,
                  (pattern.pattern_literal('cash'),),
                  (),
                  (contexts.variable('ans'),))
  
  bc_rule.bc_rule('what_to_bring_water', This_rule_base, 'what_to_bring',
                  what_to_bring_water, None,
                  (pattern.pattern_literal('water'),),
                  (),
                  (contexts.variable('ans'),))


Krb_filename = '..\\yi_rules_questions.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((20, 25), (6, 6)),
    ((38, 42), (9, 9)),
    ((44, 49), (11, 11)),
    ((50, 55), (12, 12)),
    ((68, 72), (15, 15)),
    ((74, 79), (17, 17)),
    ((80, 85), (18, 18)),
    ((98, 102), (21, 21)),
    ((104, 109), (23, 23)),
    ((110, 110), (24, 24)),
    ((123, 127), (27, 27)),
    ((129, 134), (29, 29)),
    ((135, 135), (30, 30)),
    ((148, 152), (33, 33)),
    ((154, 159), (35, 35)),
    ((160, 160), (36, 36)),
)
