import os

def check_os(os_types: list) -> str or bool:

    """
    
    Returns:
        str or bool: "posix" | "nt" | False (if doesn't match to previous OSs)
    """    
    
    recv_os = os.name
    
    if recv_os in os_types:
        
        if recv_os == os_types[0]: return os_types[0]
        if recv_os == os_types[1]: return os_types[1]
    
    return False


        
                
        
    