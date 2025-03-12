import numpy as np
import time
from mms_ok import XEM7360

def main():
    bitstream_path = r"../../bitstream/led_example.bit"

    with XEM7360(bitstream_path=bitstream_path) as fpga:
        for i in range(2**4):
            print(f"Setting LED : {np.binary_repr(i, width=4)}")
            fpga.SetLED(i)
            time.sleep(1)

if __name__ == "__main__":
    main()