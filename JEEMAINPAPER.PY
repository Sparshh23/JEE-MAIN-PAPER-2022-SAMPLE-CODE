print("JEE MAIN 2023")
questions = [
  [
    "WHICH OF THE FOLLOWING OPTIONS REPRESENTS THE UNITS OF ELECTRIC FIELD?", "V/M", "KG/M2", "KG/M2",
    "M/S" , "C"
  ],
  [
    "If momentum [P], area [A] and time [T] are taken as fundamental quantities, then the dimensional formula for the coefficient of viscosity is", "[PA–1T0]", "PAT–1]", "[PA–1T]", "[PA–1T–1]" , "A"
  ],
  [
    "Which of the following physical quantities have the same dimensions?", "Current density and surface charge density", "Electric potential and energy", "none of this",
    "Displacement current and electric field" , "C"
  ],
  [
    "A body of mass 0.5 kg travels on straight line path with velocity v = (3x2 + 4) m/s. The network done by the force during its displacement from x = 0 to x = 2 m is", "64J", "60J", "120J",
    "128J" , "B"
  ],
  [
    "Three identical particles A, B and C of mass 100 kg each are placed in a straight line with AB = BC = 13 m. The gravitational force on a fourth particle P of the same mass is F, when placed at a distance 13 m from the particle B on the perpendicular bisector of the line AC. The value of F will be approximately", "21G", "100G", "59G",
    "42G" , "B"
  ],
  [
    "A certain amount of gas of volume V at 27°C temperature and pressure 2 × 107 Nm–2 expands isothermally until its volume gets doubled. Later it expands adiabatically until its volume gets redoubled. The final pressure of the gas will be (Use, γ = 1.5)", "3.536 x 10^5 pa", "3.536 x 10^6 pa", "1.25 x 10^6 pa",
    "1.25 x 10^5 pa" , "B"
  ],
  [
    "WHICH OF THE FOLLOWING OPTIONS REPRESENTS THE UNITS OF ELECTRIC FIELD?", "V/M", "KG/M2", "KG/M2",
    "M/S" , "C"
  ],
  [
    ''' Following statements are given:

(A) The average kinetic energy of a gas molecule decreases when the temperature is reduced.

(B) The average kinetic energy of a gas molecule increases with increase in pressure at constant temperature.

(C) The average kinetic energy of a gas molecule decreases with increase in volume.

(D) Pressure of a gas increases with increase in temperature at constant pressure.

(E) The volume of gas decreases with increase in temperature.
Choose the correct answer from the options given below:
    ''', "(A)  only ", "A), (B) & (D) only ", "(B) & (D) only",
    "(A), (B) & (E) only" , "A"
  ],
  
]

QUESTIONNUMBER = [1, 2, 3, 4, 5, 6, 7, 8] 
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\n QUESTION  NUMBER  {QUESTIONNUMBER[i]}")
  print(f"{question[0]}")
  print(f"A. {question[1]} ")
  print(f"B. {question[2]} ")
  print(f"C. {question[3]} ")
  print(f"D. {question[4]} ")
  
  reply = input("ENTER YOUR ANSWER (A,B,C,D) \n" )
  if(reply == question[-1]):
    print(f"CORRECT ANSWER, YOUR NEXT QUESTIONS")
  else:
    print("Wrong answer!")
  

