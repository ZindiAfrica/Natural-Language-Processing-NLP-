#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

import sys
sys.path.append('lib')
from vecxoz_utils import compute_ensemble_cls_standalone

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

dirs = [
    'run-20210508-1501-tf-mt5large-len144-b24-7e5-4v100',
    'run-20210508-1646-tf-mt5large-len256-b24-7e5-4v100', 
    'run-20210509-1534-tf-mt5large-len64-b24-7e5-4v100',
    'run-20210509-1605-tf-mt5large-len128-b24-7e5-4p40',
    'run-20210509-1614-tf-mt5large-len192-b24-7e5-4v100',
    'run-20210509-1735-tf-mt5xl-len128-b16-7e5-1a100',
]

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

_ = compute_ensemble_cls_standalone(dirs, 
                                    data_dir='./data', 
                                    model_dir='./models', 
                                    out_dir='./',
                                    n_folds=5, 
                                    n_tta=0, 
                                    sorting='small_first', 
                                    file_name='final-submission.csv')

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
