# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_tagger_swig', [dirname(__file__)])
        except ImportError:
            import _tagger_swig
            return _tagger_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_tagger_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _tagger_swig = swig_import_helper()
    del swig_import_helper
else:
    import _tagger_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class GetMatchesParams(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GetMatchesParams, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GetMatchesParams, name)
    __repr__ = _swig_repr
    __swig_setmethods__["entity_types"] = _tagger_swig.GetMatchesParams_entity_types_set
    __swig_getmethods__["entity_types"] = _tagger_swig.GetMatchesParams_entity_types_get
    if _newclass:entity_types = _swig_property(_tagger_swig.GetMatchesParams_entity_types_get, _tagger_swig.GetMatchesParams_entity_types_set)
    __swig_setmethods__["auto_detect"] = _tagger_swig.GetMatchesParams_auto_detect_set
    __swig_getmethods__["auto_detect"] = _tagger_swig.GetMatchesParams_auto_detect_get
    if _newclass:auto_detect = _swig_property(_tagger_swig.GetMatchesParams_auto_detect_get, _tagger_swig.GetMatchesParams_auto_detect_set)
    __swig_setmethods__["allow_overlap"] = _tagger_swig.GetMatchesParams_allow_overlap_set
    __swig_getmethods__["allow_overlap"] = _tagger_swig.GetMatchesParams_allow_overlap_get
    if _newclass:allow_overlap = _swig_property(_tagger_swig.GetMatchesParams_allow_overlap_get, _tagger_swig.GetMatchesParams_allow_overlap_set)
    __swig_setmethods__["find_acronyms"] = _tagger_swig.GetMatchesParams_find_acronyms_set
    __swig_getmethods__["find_acronyms"] = _tagger_swig.GetMatchesParams_find_acronyms_get
    if _newclass:find_acronyms = _swig_property(_tagger_swig.GetMatchesParams_find_acronyms_get, _tagger_swig.GetMatchesParams_find_acronyms_set)
    __swig_setmethods__["protect_tags"] = _tagger_swig.GetMatchesParams_protect_tags_set
    __swig_getmethods__["protect_tags"] = _tagger_swig.GetMatchesParams_protect_tags_get
    if _newclass:protect_tags = _swig_property(_tagger_swig.GetMatchesParams_protect_tags_get, _tagger_swig.GetMatchesParams_protect_tags_set)
    __swig_setmethods__["tokenize_characters"] = _tagger_swig.GetMatchesParams_tokenize_characters_set
    __swig_getmethods__["tokenize_characters"] = _tagger_swig.GetMatchesParams_tokenize_characters_get
    if _newclass:tokenize_characters = _swig_property(_tagger_swig.GetMatchesParams_tokenize_characters_get, _tagger_swig.GetMatchesParams_tokenize_characters_set)
    __swig_setmethods__["max_tokens"] = _tagger_swig.GetMatchesParams_max_tokens_set
    __swig_getmethods__["max_tokens"] = _tagger_swig.GetMatchesParams_max_tokens_get
    if _newclass:max_tokens = _swig_property(_tagger_swig.GetMatchesParams_max_tokens_get, _tagger_swig.GetMatchesParams_max_tokens_set)
    def __init__(self): 
        this = _tagger_swig.new_GetMatchesParams()
        try: self.this.append(this)
        except: self.this = this
    def add_entity_type(self, *args): return _tagger_swig.GetMatchesParams_add_entity_type(self, *args)
    __swig_destroy__ = _tagger_swig.delete_GetMatchesParams
    __del__ = lambda self : None;
GetMatchesParams_swigregister = _tagger_swig.GetMatchesParams_swigregister
GetMatchesParams_swigregister(GetMatchesParams)

class Tagger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tagger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tagger, name)
    __repr__ = _swig_repr
    __swig_setmethods__["serials_only"] = _tagger_swig.Tagger_serials_only_set
    __swig_getmethods__["serials_only"] = _tagger_swig.Tagger_serials_only_get
    if _newclass:serials_only = _swig_property(_tagger_swig.Tagger_serials_only_get, _tagger_swig.Tagger_serials_only_set)
    __swig_setmethods__["organisms"] = _tagger_swig.Tagger_organisms_set
    __swig_getmethods__["organisms"] = _tagger_swig.Tagger_organisms_get
    if _newclass:organisms = _swig_property(_tagger_swig.Tagger_organisms_get, _tagger_swig.Tagger_organisms_set)
    def __init__(self, *args): 
        this = _tagger_swig.new_Tagger(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _tagger_swig.delete_Tagger
    __del__ = lambda self : None;
    def add_name(self, *args): return _tagger_swig.Tagger_add_name(self, *args)
    def allow_block_name(self, *args): return _tagger_swig.Tagger_allow_block_name(self, *args)
    def check_name(self, *args): return _tagger_swig.Tagger_check_name(self, *args)
    def is_blocked(self, *args): return _tagger_swig.Tagger_is_blocked(self, *args)
    def resolve_name(self, *args): return _tagger_swig.Tagger_resolve_name(self, *args)
    def load_global(self, *args): return _tagger_swig.Tagger_load_global(self, *args)
    def load_local(self, *args): return _tagger_swig.Tagger_load_local(self, *args)
    def load_names(self, *args): return _tagger_swig.Tagger_load_names(self, *args)
    def get_matches(self, *args): return _tagger_swig.Tagger_get_matches(self, *args)
Tagger_swigregister = _tagger_swig.Tagger_swigregister
Tagger_swigregister(Tagger)


def quit():
  return _tagger_swig.quit()
quit = _tagger_swig.quit

