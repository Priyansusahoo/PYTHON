print('''

                          __..__             
                      _.sMSMMMMMMb.          
                   .-"TMMMMSMMMMMMMb.    
                 .'    TMMMMSMMMMMMMMb       
                /       TMMMSMMMMMMSSS;      
               :        :MMMMSMMMSSMMMM;     
               ;       @ MMMMSMMSMMMMMMS     
              :    _,   ,P"TMSMSMMMMMMSM     
              : .+""`,  :    `TMMMMMSSMM     
               ) c),     `-,-=,TSSSSMMMM     
              /  `         ,-;|MMMMMMMM;     
             /     _.'(o)  '-';SMSSSSSS      
            (  ,   o       ,-"'`^MMMM'       
             )`            :`.    .'         
             )-.           ;  `- /           
             \         _.-'     :            
             (     _.-"   `.     \           
              "---"--.      \     \          
                      `.     \     \         
                   bug  \       _.sSb        
                         \ _.sSSSSSSSb       
                         dSSSSSSSSP^" \      
                         SSSP^" ___    \     
                        /    .gP""""Tp. \    
                       :    d'     .  `b \   
                       ;   d'       o  `b ;  
                      /   d;            `b|  
                     /,   $;          @  `:  
                    /'    $$               ; 
                  .'      $$b         (o)  | 
                .'       d$$$;             : 
               /       .d$$$$;          ,   ;
              d      .d$$$$$$$          $   |
             :bp.__.g$$$$$$$$$         :$   ;
             $$$$$$$$$$$$$$$$$         $$b : 

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

D1 = input("which direction do you want to go, LEFT or RIGHT\n")
d1 = D1.lower()

if d1 == "right":
  print("Fall into a hole. Game Over.")
elif d1 == "left":
  D2 = input("You arrived in a island, do you want to WAIT or SWIM\n")
  d2 = D2.lower()
  if d2 == "swim":
    print("Attacked by trout.GAME OVER")
  elif d2 == "wait":
    D3 = input("You arrived in a house with three doors of color BLUE, RED, YELLOW\n")
    d3 = D3.lower()
    if d3 == "red":
      print("Burned by fire.GAME OVER")
    elif d3 == "blue":
      print("Eaten by beast.GAME OVER")
    elif d3 == "yellow":
      print("You win..Congo!!")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload



