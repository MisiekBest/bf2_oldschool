# bf2_oldschool
BF2 Oldschool is a Battlefield 2 python script made for restricting weapons.


 How to install: 

 1. Go to mods/bf2/python/game/ direcory located on your server 
 (ex. BF2_v1.1.2965/mods/bf2/python/game/)                      
 2. Paste there this file                                       
 3. Edit __init__.py file and add this two lines:               
 import bf2_oldschool                                           
 bf2_oldschool.init()                                           
 4. Restart/run your server :)                                  




 How to manage sctipt via rcon?: 

 This script has 'diffrent' manage method. Why diffrent?                                     
 Usually admins can manage their scripts using in game chat.                                 
 Yes, its easiest way, but not efficient. So i decided to use                                
 little hook with rcon <variable>. It will always generate info                              
 about error (in game console) but it will work!                                             
                                                                                             
 First you must remember to put your/admin's nickname in settings.                           
 Rcon will work only for players that are in ADMIN_LIST.                                     
 See ADMIN SETTINGS section for more info.                                                   
                                                                                             
 TO RUN COMMAND:                                                                             
                                                                                             
 1. Open your in-game console (by pressing ~ on your keyboard)                               
 2. Every command you must execute using phrase: rcon bfo <command> <optional_value>         
                                                                                             
 You can access to this help in game by using 'rcon bfo help' command.                       
 You can return all main settings by using 'rcon bfo status' command.                        
                                                                                             
 Here is list of all commands:                                                               
  OLDSCHOOL LEVEL                                                
                                                
 olevel          Return number of oldschool level                                           
 olevel [value]  Set oldschool level to given value                                         
                                                                                             
  PUNISH METHOD                                                  
                                                 
 punish          Return number of punish method                                             
 punish [value]  Set punish method to given value                                           
                                                                                             
    MISC WEAPONS                                                 
                                               
 c4          Return status of C4 restriction                                                
 c4 [value]  Enable or disble C4 restriction. 0-Disable  1-Enable                           
 claymore          Return status of CLAYMORE restriction                                    
 claymore [value]  Enable or disble CLAYMORE restriction. 0-Disable  1-Enable               
 mgs          Return status of MOUNTED MGS restriction                                      
 mgs [value]  Enable or disble MOUNTED MGS restriction. 0-Disable  1-Enable                 
 tow          Return status of TOW MISSILE restriction                                      
 tow [value]  Enable or disble TOW MISSILE restriction. 0-Disable  1-Enable                 
                                                                                             
    KICKER SYSTEM (punish 2)                                     
                                   
 kick_frags          Return number of how many kills from restricted weapon to kick player  
 kick_frags [value]  Set HOW_MANY_KILLS_TO_KICK to given value                              
 kick_time           Return minutes for how long player should be kicked out.               
 kick_time [value]   Set minutes for how long player should be kicked out.                  
                                                                                             
     ANTI COMMANDER                                              
                                           
 anticomm            Return status of ANTICOMMANDER system                                  
 anticomm [value]    Enable or disble commander restriction. 0-Disable  1-Enable            
 commkick            Return status of COMMANDER KICKER system                               
 commkick [value]    Enable or disble commander kicking. 0-Disable  1-Enable                
 commkick_time           Return minutes for how long commander should be kicked out.        
 commkick_time [value]   Set minutes for how long commander should be kicked out.           
                                                                                              
                                                                                             


CHANGELOG:

0.9c:
- Added "NO SNIPERS" restriction mode (OLDSCHOOL_LEVEL = 6)
