import cProfile
import profile
import re

cProfile.run('re.compile("foo|bar")', 'restats')