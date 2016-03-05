#    mergeable mixin - support to use of mixins in django models or other 
#    types of classes
#    Copyright (C) 2016  Jean Jung
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

""" mergeable mixins adds support to use of mixins in django models or other 
    types of classes.    
    The key idea here is that it removes the attribute lookup problem of the 
    multiple inheritance, and let you choose from what mixin you want to copy 
    functionalities
"""

import copy

class merge_mixins(object):
    """ Defines a list of source mixins to be merged on the class.
        You can choose what mixins to copy and what will be the priority, 
        specifying the mixin with the greater priority first, so if you have 
        two mixins that  implements the method __unicode__ for example, just the 
        first will be copied.
    """
    def __init__(self, *args, **kwargs):
        self.mixins = args
    
    def __call__(self, target):
        for mixin in self.mixins:
            for (name, attr) in mixin.__dict__.items():
                if not hasattr(target, name):
                    # Django models needs this to make some magic
                    # with the Fields classes.
                    if hasattr(attr, 'contribute_to_class'):
                        copy.deepcopy(attr).contribute_to_class(target, name)
                    else:
                        setattr(target, name, copy.deepcopy(attr))
        return target
