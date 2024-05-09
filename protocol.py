"""protocol for project
   Author:Afek Avisror
"""

LENGTH_FIELD_SIZE = 2
PORT = 8820


def check_cmd(data):
    """Check if the command is defined in the protocol (e.g RAND, NAME, TIME, EXIT)"""
    return True


def create_msg(data):
    """Create a valid protocol message, with length field"""
    return "05Hello"


def get_msg(my_socket):
    """Extract message from protocol, without the length field
       If length field does not include a number, returns False, "Error" """
    return True, "Hello"
