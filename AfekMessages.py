__author__ = "Afek"

# from  tcp_by_size import send_with_size ,recv_by_size


SIZE_HEADER_FORMAT = "000000|"  # n digits for data size + one delimiter
size_header_size = len(SIZE_HEADER_FORMAT)
TCP_DEBUG = True
LEN_TO_SEND = 10000


def recv_by_size(sock):
    size = sock.recv(size_header_size)
    size = (size[: size_header_size - 1]).decode()
    try:
        size = int(size)
    except:
        return "ERROR size not int"
    header = sock.recv(size).decode()
    bdata = b""
    while True:
        size = sock.recv(size_header_size)
        size = (size[: size_header_size - 1]).decode()
        try:
            size = int(size)
        except:
            return "ERROR size not int"
        crn = sock.recv(size)
        if crn.decode() == "END":
            return header, bdata
        bdata += crn


def send_with_size(sock, bdata, header):  # the size of header here is constant 6
    if type(bdata) == str:
        bdata = bdata.encode()
    if type(header) == str:
        bdata = header.encode()
    msg = (f"{len(header):06d}" + "|").encode() + header
    sock.send(msg)
    sent_size = 0
    while sent_size < len(bdata):
        this_round_data_size = min(LEN_TO_SEND, len(bdata) - sent_size)
        msg = (f"{this_round_data_size:06d}" + "|").encode() + bdata[
            sent_size : sent_size + this_round_data_size
        ]
        sock.send(msg)
        sent_size += this_round_data_size
    msg = (f"{len(header):06d}" + "|END").encode()
    sock.send(msg)
    return
