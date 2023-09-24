; Define global variables
global toggleRightClickHold := false

RButton::
    if GetKeyState("RButton", "P")
    {
        toggleRightClickHold := !toggleRightClickHold
        if (toggleRightClickHold)
        {
            Click down right 
        }
        else
        {
            Click up right 
        }
    }
return

;checkpoint
]::
	ExitApp
return