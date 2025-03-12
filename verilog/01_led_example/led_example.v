module led_example(
    input   wire [4:0]  okUH,
    output  wire [2:0]  okHU,
    inout   wire [31:0] okUHU,
    inout   wire        okAA,

    output  wire [3:0]  led
);

// Target interface bus
wire            okClk;
wire [112:0]    okHE;
wire [64:0]     okEH;

// Endpoint connections
wire [32 - 1:0] ep00wire;

function [3:0] xem7360_led;
input [3:0] a;
integer i;
begin
    for(i = 0; i < 4; i = i + 1) begin
        xem7360_led[i] = (a[i] == 1'b1) ? 1'b0 : 1'bz;
    end
end
endfunction

assign led = xem7360_led(ep00wire[3:0]);

okHost okHI(
    .okUH(okUH),
    .okHU(okHU),
    .okUHU(okUHU),
    .okAA(okAA),
    .okClk(okClk),
    .okHE(okHE),
    .okEH(okEH)
);

okWireIn ep00 (.okHE(okHE), .ep_addr(8'h00), .ep_dataout(ep00wire));

endmodule