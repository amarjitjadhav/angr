# Microsoft Visual C/C++ Runtime
from . import SimLibrary
from .. import SIM_PROCEDURES as P

libc = SimLibrary()
libc.set_library_names('msvcr100.dll', 'msvcr110.dll')
libc.add_all_from_dict(P['msvcr'])
libc.set_non_returning('_exit', 'abort', 'exit', '_invoke_watson')

libc.add_alias('_initterm', '_initterm_e')

libc.add_all_from_dict(P['libc'])
