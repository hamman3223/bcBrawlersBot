import platform


def check_os(os_types: list) -> str or bool:

    """

    Returns:
        str or bool: "Darwin" | "Linux" | "nt" | False (if doesn't match to previous OSs)
    """

    recv_os = platform.system()

    if recv_os in os_types:

        if recv_os == os_types[0]: return os_types[0]
        if recv_os == os_types[1]: return os_types[1]
        if recv_os == os_types[2]: return os_types[2]

    return False
