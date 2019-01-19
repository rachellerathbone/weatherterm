# This is the app's parser loader
import os
import re
import inspect

# First this function is executed and returns a list of of all files located
# in weatherterm/parsers. It will filter the files based on the rules of the
# parser loader.
def _get_parser_list(dirname):
    files = [f.replace('.py', '')
             for f in os.listdir(dirname)
             if not f.startswith('__')]
    return files

# After returning the files this function imports the module. It first imports
# the weatherterm.parsers module and makes use of the inspect package in the
# standard library to find the parser classes within the module.
def _import_parsers(parserfiles):
    m = re.compile('.+parser$', re.I)
    _modules = __import__('weatherterm.parsers',
                          globals(),
                          locals(),
                          parserfiles,
                          0)

    # Inspect.getmembers returns a list of tuples where the first item is a key
    # representing a property in the module, and the second item is the value,
    # which can be of any type. In our scenario, we are interested in a property
    # with a key ending with parser and with the value of type class.
    _parsers = [(k, v) for k, v in inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]
    _classes = dict()

    # Loops through the items in the module and extract the parser classes,
    # returning a dictionary containing the name of the class object that will
    # be later used to create instances of the parser.
    for k, v in _parsers:
        _classes.update({k: v for k, v in inspect.getmembers(v)
                         if inspect.isclass(v) and m.match(k)})
        return _classes


def load(dirname):
    parserfiles = _get_parser_list(dirname)
    return _import_parsers(parserfiles)
