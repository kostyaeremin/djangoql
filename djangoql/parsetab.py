
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionCOMMA OR AND NOT IN TRUE FALSE NONE NAME STRING_VALUE FLOAT_VALUE INT_VALUE PAREN_L PAREN_R EQUALS NOT_EQUALS GREATER GREATER_EQUAL LESS LESS_EQUAL CONTAINS NOT_CONTAINS\n        expression : PAREN_L expression PAREN_R\n        \n        expression : expression logical expression\n        \n        expression : name comparison_number number\n                   | name comparison_string string\n                   | name comparison_equality boolean_value\n                   | name comparison_equality none\n                   | name comparison_in_list const_list_value\n        \n        name : NAME\n        \n        logical : AND\n                | OR\n        \n        comparison_number : comparison_equality\n                          | comparison_greater_less\n        \n        comparison_string : comparison_equality\n                          | comparison_greater_less\n                          | comparison_contains\n        \n        comparison_equality : EQUALS\n                            | NOT_EQUALS\n        \n        comparison_greater_less : GREATER\n                                | GREATER_EQUAL\n                                | LESS\n                                | LESS_EQUAL\n        \n        comparison_contains : CONTAINS\n                            | NOT_CONTAINS\n        \n        comparison_in_list : IN\n                           | NOT IN\n        \n        const_value : number\n                    | string\n                    | none\n                    | boolean_value\n        \n        number : INT_VALUE\n        \n        number : FLOAT_VALUE\n        \n        string : STRING_VALUE\n        \n        none : NONE\n        \n        boolean_value : true\n                      | false\n        \n        true : TRUE\n        \n        false : FALSE\n        \n        const_list_value : PAREN_L const_value_list PAREN_R\n        \n        const_value_list : const_value_list COMMA const_value\n        \n        const_value_list : const_value\n        '
    
_lr_action_items = {'PAREN_L':([0,2,5,6,7,12,17,41,],[2,2,2,-9,-10,40,-24,-25,]),'NAME':([0,2,5,6,7,],[4,4,4,-9,-10,]),'$end':([1,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,48,],[0,-2,-1,-3,-30,-31,-4,-32,-5,-6,-34,-35,-33,-36,-37,-7,-38,]),'AND':([1,8,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,48,],[6,6,6,-1,-3,-30,-31,-4,-32,-5,-6,-34,-35,-33,-36,-37,-7,-38,]),'OR':([1,8,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,48,],[7,7,7,-1,-3,-30,-31,-4,-32,-5,-6,-34,-35,-33,-36,-37,-7,-38,]),'EQUALS':([3,4,],[15,-8,]),'NOT_EQUALS':([3,4,],[16,-8,]),'IN':([3,4,18,],[17,-8,41,]),'NOT':([3,4,],[18,-8,]),'GREATER':([3,4,],[19,-8,]),'GREATER_EQUAL':([3,4,],[20,-8,]),'LESS':([3,4,],[21,-8,]),'LESS_EQUAL':([3,4,],[22,-8,]),'CONTAINS':([3,4,],[23,-8,]),'NOT_CONTAINS':([3,4,],[24,-8,]),'PAREN_R':([8,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,42,43,44,45,46,47,48,50,],[26,-2,-1,-3,-30,-31,-4,-32,-5,-6,-34,-35,-33,-36,-37,-7,48,-40,-26,-27,-28,-29,-38,-39,]),'INT_VALUE':([9,11,13,15,16,19,20,21,22,40,49,],[28,-11,-12,-16,-17,-18,-19,-20,-21,28,28,]),'FLOAT_VALUE':([9,11,13,15,16,19,20,21,22,40,49,],[29,-11,-12,-16,-17,-18,-19,-20,-21,29,29,]),'STRING_VALUE':([10,11,13,14,15,16,19,20,21,22,23,24,40,49,],[31,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,31,31,]),'NONE':([11,15,16,40,49,],[36,-16,-17,36,36,]),'TRUE':([11,15,16,40,49,],[37,-16,-17,37,37,]),'FALSE':([11,15,16,40,49,],[38,-16,-17,38,38,]),'COMMA':([28,29,31,34,35,36,37,38,42,43,44,45,46,47,50,],[-30,-31,-32,-34,-35,-33,-36,-37,49,-40,-26,-27,-28,-29,-39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,5,],[1,8,25,]),'name':([0,2,5,],[3,3,3,]),'logical':([1,8,25,],[5,5,5,]),'comparison_number':([3,],[9,]),'comparison_string':([3,],[10,]),'comparison_equality':([3,],[11,]),'comparison_in_list':([3,],[12,]),'comparison_greater_less':([3,],[13,]),'comparison_contains':([3,],[14,]),'number':([9,40,49,],[27,44,44,]),'string':([10,40,49,],[30,45,45,]),'boolean_value':([11,40,49,],[32,47,47,]),'none':([11,40,49,],[33,46,46,]),'true':([11,40,49,],[34,34,34,]),'false':([11,40,49,],[35,35,35,]),'const_list_value':([12,],[39,]),'const_value_list':([40,],[42,]),'const_value':([40,49,],[43,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> PAREN_L expression PAREN_R','expression',3,'p_expression_parens','parser.py',49),
  ('expression -> expression logical expression','expression',3,'p_expression_logical','parser.py',55),
  ('expression -> name comparison_number number','expression',3,'p_expression_comparison','parser.py',61),
  ('expression -> name comparison_string string','expression',3,'p_expression_comparison','parser.py',62),
  ('expression -> name comparison_equality boolean_value','expression',3,'p_expression_comparison','parser.py',63),
  ('expression -> name comparison_equality none','expression',3,'p_expression_comparison','parser.py',64),
  ('expression -> name comparison_in_list const_list_value','expression',3,'p_expression_comparison','parser.py',65),
  ('name -> NAME','name',1,'p_name','parser.py',71),
  ('logical -> AND','logical',1,'p_logical','parser.py',77),
  ('logical -> OR','logical',1,'p_logical','parser.py',78),
  ('comparison_number -> comparison_equality','comparison_number',1,'p_comparison_number','parser.py',84),
  ('comparison_number -> comparison_greater_less','comparison_number',1,'p_comparison_number','parser.py',85),
  ('comparison_string -> comparison_equality','comparison_string',1,'p_comparison_string','parser.py',91),
  ('comparison_string -> comparison_greater_less','comparison_string',1,'p_comparison_string','parser.py',92),
  ('comparison_string -> comparison_contains','comparison_string',1,'p_comparison_string','parser.py',93),
  ('comparison_equality -> EQUALS','comparison_equality',1,'p_comparison_equality','parser.py',99),
  ('comparison_equality -> NOT_EQUALS','comparison_equality',1,'p_comparison_equality','parser.py',100),
  ('comparison_greater_less -> GREATER','comparison_greater_less',1,'p_comparison_greater_less','parser.py',106),
  ('comparison_greater_less -> GREATER_EQUAL','comparison_greater_less',1,'p_comparison_greater_less','parser.py',107),
  ('comparison_greater_less -> LESS','comparison_greater_less',1,'p_comparison_greater_less','parser.py',108),
  ('comparison_greater_less -> LESS_EQUAL','comparison_greater_less',1,'p_comparison_greater_less','parser.py',109),
  ('comparison_contains -> CONTAINS','comparison_contains',1,'p_comparison_contains','parser.py',115),
  ('comparison_contains -> NOT_CONTAINS','comparison_contains',1,'p_comparison_contains','parser.py',116),
  ('comparison_in_list -> IN','comparison_in_list',1,'p_comparison_in_list','parser.py',122),
  ('comparison_in_list -> NOT IN','comparison_in_list',2,'p_comparison_in_list','parser.py',123),
  ('const_value -> number','const_value',1,'p_const_value','parser.py',132),
  ('const_value -> string','const_value',1,'p_const_value','parser.py',133),
  ('const_value -> none','const_value',1,'p_const_value','parser.py',134),
  ('const_value -> boolean_value','const_value',1,'p_const_value','parser.py',135),
  ('number -> INT_VALUE','number',1,'p_number_int','parser.py',141),
  ('number -> FLOAT_VALUE','number',1,'p_number_float','parser.py',147),
  ('string -> STRING_VALUE','string',1,'p_string','parser.py',153),
  ('none -> NONE','none',1,'p_none','parser.py',159),
  ('boolean_value -> true','boolean_value',1,'p_boolean_value','parser.py',165),
  ('boolean_value -> false','boolean_value',1,'p_boolean_value','parser.py',166),
  ('true -> TRUE','true',1,'p_true','parser.py',172),
  ('false -> FALSE','false',1,'p_false','parser.py',178),
  ('const_list_value -> PAREN_L const_value_list PAREN_R','const_list_value',3,'p_const_list_value','parser.py',184),
  ('const_value_list -> const_value_list COMMA const_value','const_value_list',3,'p_const_value_list','parser.py',190),
  ('const_value_list -> const_value','const_value_list',1,'p_const_value_list_single','parser.py',196),
]
