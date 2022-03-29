import imp
#import printing_models

#from printing_models import print_models , show_completed_models 
from printing_models import print_models as pm, show_completed_models as sm

#import printing_models as pm 

# from printing_models import *

un_designed = ['phone case', 'robot pendant', 'dodecaherdon']
completed_design = []

pm(unprinted_designs=un_designed, completed_models=completed_design)
sm(completed_models=completed_design)