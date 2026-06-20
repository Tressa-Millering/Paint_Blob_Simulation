# Paint Blob Simulation
This script simulates dropping red, green, or blue paint blobs onto an empty canvas.  
Each tick, a blob is dropped at a random location, overwriting any prior paint. Multiple
experiments are run using parameters provided by the user.    							  

> Note: This is a fork of the original working repository, as the original used my academic account.
> While I have made changes to the README and removed some of our test files, the actual script remains the same.

## Authors
- Tressa Millering   
- Tori St. John      
- Matthew Yeager     
- Jacob Young

## Program Description				
This script simulates dropping red, green, or blue paint blobs onto an empty canvas.
Each tick, a blob is dropped at a random location, overwriting any prior paint. 
Multiple experiments are run using parameters provided by the user.                                  
                                                                                            
On first run, an example simulation drops 300 blobs onto a 10x10 grid. Stats are shown 
up to twice: once when every cell has been covered for the first time (if ever), and once
after the 300th blob drops.                                                                 
                                                                                            
After the example, the user is prompted to enter:  
- N — the grid size for the next simulation                                               
- T — the number of blob drops to simulate                                                
                                                                                          
A new simulation runs with these constraints, followed by a batch of 10 simulations in 
which the user chooses to increment either N or T each run. When all 10 are complete,
stats across the batch are displayed as a graph, and the program ends.                    										  

## Major Packages Used
- TKinter	
- Matplotlib	
