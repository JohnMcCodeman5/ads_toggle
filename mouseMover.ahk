#Persistent 
; SetMouseDelay, 20

global toggle := false

Loop
{
    if (toggle){
    ; Move the mouse right
    MouseMove, 200, 0, 10, R

    MouseMove, 0, -200, 10, R

    MouseMove, -200, 0, 10, R

    MouseMove, 0, 200, 10, R
   }   

}

q:: ExitApp

p:: toggle := !toggle