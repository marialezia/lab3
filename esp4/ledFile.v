`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 12/13/2022 03:35:56 PM
// Design Name: 
// Module Name: ledFile
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module ledFile(
////////////////////
       //input clk ,
       //output reg [7:0] LED
//  ) ;
  //  reg counter ;
   // initial
   // counter = 0;
   // always @ ( posedge clk ) begin
   // LED [0] <= counter ;
    //counter <= counter + 1;
    // end
    
    ////////////
    // 2 HZ
    //input clk ,
//output reg [7:0] LED
//) ;
//reg [32:0] counter ;
//initial
//counter = 0;
//always @ ( posedge clk ) begin
//LED [0] <= counter[23];
//counter <= counter + 1;
//end



//////////////
//if primo interruttore aperto

    //input clk ,
    //input [7:0] sw,
//output reg [7:0] LED
//) ;
//reg [32:0] counter ;
//initial
//counter = 0;
//always @ ( posedge clk ) begin
//if(sw[0]==1)
//begin
//LED [0] <= counter[23];
//counter <= counter + 1;
//end
//else
//begin 

//end

//end

    
 //////////
 //Binary counter 16 Led
    
    //input clk ,
    //input [7:0] sw,
//output reg [7:0] LED
//) ;
//reg [40:0] counter ;
//integer i;
//initial
//counter = 0;
//always @ ( posedge clk ) begin
  // if(sw[0]==1)
  // begin
   //counter <= counter + 1;
  // for(i=0 ; i < 16; i=i+1) begin
  // LED [i] <= counter[23 + i];
  // end
//end
//else
//begin 

//end

//end

/////////
//if click tasto centrale accendo o spengo led

    //input clk ,
    //input btnC,
//output reg [7:0] LED
//) ;
//reg counter ;
//reg oldbtnC ;

//always @ ( posedge clk ) begin
    //oldbtnC <= btnC;

    //if((btnC != oldbtnC) && (btnC ==1))
    //begin
//        counter <= counter + 1;
  //  end
    
   // LED[0] <= counter;
//end

////////

  input clk ,
  input btnL,
  input btnR,
output reg [15:0] LED
) ;
reg counter ;
reg oldbtnR ;
reg oldbtnL ;
integer i ;
reg [15:0] statoled;
initial
statoled[8]<= 1;
always @ ( posedge clk ) begin
    oldbtnR<= btnR;
    oldbtnL<= btnL;
    if(btnR != oldbtnR & btnR==1) begin 
        for (i=0;i<16; i=i+1)begin
            if(statoled[i]==1)
            begin
            statoled[i]=statoled[i]+1;
            statoled[i+1]=statoled[i+1]+1;
            end
        end
    end
    if(btnL != oldbtnL & btnL==1) begin 
        for (i=0;i<16; i=i+1)begin
            if(statoled[i]==1)
            begin
            statoled[i]=statoled[i]+1;
            statoled[i-1]=statoled[i-1]+1;
            end
        end
        end
    LED<=statoled;
end
endmodule
