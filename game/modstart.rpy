init -100 python:
    config.label_overrides["start"] = "mod_start"

label mod_start:  
  
    scene bg club_day  
    show monika 3b at t11  
  
    m "Settle down, everyone!"  
    m 4k "It's time to build the mod we talked about earlier!"  
  
    show monika 4a at t21  
    show natsuki 4e at t22  
    n "Wait, we're actually doing this now?!"  
  
    show monika 4a at t31  
    show natsuki 1g at t32  
    show yuri 2r at t33  
    y "Yes, Natsuki."  
  
    show natsuki 1o at t32  
    y 2h "Unless you want to quit?"  
    n 1p "Hah! As if I'd quit now."  
    n 5q "I just didn't think we'd actually get started this soon."  
    return  
