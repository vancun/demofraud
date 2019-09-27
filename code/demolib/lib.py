from .democonfig import cfg
import os

def flag_make_file_name(flag_name):
    return "{}/__{}__".format(cfg.flags_dir, flag_name)

def flag_poll(flag_name, clear_on_poll=False):
    flag_fname = flag_make_file_name(flag_name)
    poll_result = os.path.isfile(flag_fname)
    if poll_result and clear_on_poll:
        flag_clear(flag_name)
    return poll_result

def flag_clear(flag_name):
    flag_fname = flag_make_file_name(flag_name)
    os.remove(flag_fname)

def is_in_databricks():
  return 'DATABRICKS_RUNTIME_VERSION' in os.environ


__all__ = ['flag_poll', 'flag_clear', 'is_in_databricks']


