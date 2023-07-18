
print('🤔 Thinking… 🤔')

pkg = 'parent'
mdl = 'test_step2'

print("Hi! I'm in " + pkg + '.' + mdl + '!')

import pkg_a
import pkg_b
import pkg_z

print('\n\n🟥 ERROR: Inaccurate or unreliable results.\n'
      '\n'
      'PROBLEM: Imported modules in same directory (i.e. namespace) as'
      ' executed module (i.e. parent) during package __init__s because'
      ' identically named modules within packages (e.g. mdl_a,'
      ' pkg_a.mdl_a, pkg_b.mdl_a). Unable to specify package namespace'
      ' during package __init__ imports. Created namespace conflicts'
      ' for identically named modules within different packages'
      ' (e.g. mdl_a, pkg_a.mdl_a, pkg_b.mdl_a). Imported similarly'
      ' named modules in highest package (i.e. parent directory and'
      ' namespace) (e.g. mdl_a, mdl_b, mdl_z) and ignored similarly'
      ' named modules in lower packages (e.g. pkg_a, pkg_b, pkg_z).\n'
      '\n'
      'SOLUTION: Import fully qualified namespaced modules within'
      ' each module (e.g. mdl_a, pkg_a.mdl_a, pkg_b.mdl_a). Do not'
      ' use package __init__s to bundle package module imports.'
      ' Package __init__s should contain docstring but no code.')