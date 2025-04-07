from mms_ok import XEM7360


def single_transfer(fpga, reorder_str: bool = True):
    data = "000102030405060708090A0B0C0D0E0F"
    print(f"Data: {data} [{type(data)}]")

    write_transfer_byte = fpga.WriteToPipeIn(0x80, data, reorder_str=reorder_str)
    print(f"Write transfer byte: {write_transfer_byte} Bytes")

    read_data = fpga.ReadFromPipeOut(0xA0, 128 // 8, reorder_str=reorder_str)
    print(f"Read data: {read_data} [{type(read_data)}]")
    print(f"Read transfer byte: {read_data.transfer_byte} Bytes")


def multiple_transfer(fpga, num_transfer: int, reorder_str: bool = True):
    from secrets import token_hex

    for i in range(num_transfer):
        data = token_hex(128 // 8)
        print(f"[Transfer {i}] Data: {data} [{type(data)}]")

        write_transfer_byte = fpga.WriteToPipeIn(0x80, data, reorder_str=reorder_str)
        print(f"[Transfer {i}] Write transfer byte: {write_transfer_byte} Bytes")

    for i in range(num_transfer):
        read_data = fpga.ReadFromPipeOut(0xA0, 128 // 8, reorder_str=reorder_str)
        print(f"[Transfer {i}] Read data: {read_data} [{type(read_data)}]")
        print(f"[Transfer {i}] Read transfer byte: {read_data.transfer_byte} Bytes")


def main():
    bitstream_path = r"../../bitstream/fifo_example.bit"

    with XEM7360(bitstream_path=bitstream_path) as fpga:
        fpga.reset()

        # single_transfer(fpga)
        multiple_transfer(fpga, num_transfer=10)


if __name__ == "__main__":
    main()
