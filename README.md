# mlassign5
malnutrition assessment
PROJECT NAME - MALNUTRITION ASSESSMENT

     An attempt to identify malnutrition like IUGR , MARASMUS and KWASHIORKOR using machine learning.
DATASET:

    Dataset named pem.csv which was created by me, contains 13 attributes(13 column) which intern helps to find out the malnutrition.
    
    The attributes are -  1.id
                          2.age_inmonths
                          3.birth_weight
                          4.appetite
                          5.edema
                          6.skin_changes
                          7.phychomotor_changes
                          8.serum_albumin_level
                          9.abdomen
                          10.organomegaly
                          11.subcutaneous_fat
                          12.present_weight
                          13.diagnosis
               
    1.id - it just gives the serial number to the rows.
    
    2.age_inmonths - it gives the age of the patients in months.
    
    3.birth_weight - it gives the weight of the baby during birth.
    
    4.appetite - hunger for food in an individual, it can be, i)varacious - appetite more than normal.
                                                              ii)poor - appetite below normal.
                                                              iii)good - appetite normal.
                                                              
    5.edema - swelling caused by excess fluid trapped in your body tissue, it can i)present - edema present.
                                                                                  ii)negative - edema not present.
                                                                                  
    6.skin_changes - any changes in appearance of the skin, it can be, i)dry_scaly - skin is dry and the texture would be like fish scale.
                                                                       ii)dermatosis - any other alternation in skin like redness which doesn't cause inflamation.
                                                                       iii)no - no skin changes.
                                                                       
    7.phychomotor_changes - behaviuoral changes, it can be, i)irritable - 
                                                            ii)lethargic - feeling dull in all the activities.
                                                            iii)no - no any changes.
   
    8.serum_albumin_level - it measures the amount of protein in individuals blood. It can vary from 3.4 to 5.4g/dL.
    
    9.abdomen - it access the abdomenal changes, it can be, i)distended - abdomen swollen.
                                                            ii)normal - abdomen normal.
                                                          
    10.organomegaly - here we access major abdomenal organs including spleen, liver, kidney etc., it can be, i)yes - increased in size
                                                                                                             ii)no - normal.
                                                                                                             
    11.subcutaneous_fat - fatty tissue present beneath the skin. here we are accessing subcutaneous fat using calipers, usually it is accessed between the age group of 0-10                               age and its values varies from 0 to 30.
    
    12.present_weight - present weight of the individual.
    
    13.diagnosis - 
                  
                 a) IUGR - It stands for intra uterine growth retardation. It refers to a condition in which an unborn baby is smaller than it should be because it is not growing at a normal rate inside the womb. First 50 entries in dataset denotes IUGR i.e fron id 1 to 50. The main parameter to identify this malnutrition is the birth weight, which will be below 2.5. 
                 
                 b)MERASMUS - It is a form of malnutrition. It happens when the intake of nutrients and energy is too low for a person’s needs. It leads to wasting, or       the loss of body fat and muscle. A child with marasmus may not grow as children usually do. Next 50 entries in dataset denotes MERASMUS i.e from id 51 to 100. The parameters to identify this malnutrition will be weight lose more than 30% compared to normalhealthy child of the similar age group(normal weight calculation, for 0-3months weight=birthweight+30*age_in_days, for 3months to 1 year weight=(age_in_months+9)/2, for 1 to 6 years weight=age*2+8), its major symptom being high increase in appetite, increase in irritability, loss of subcutaneous fat,dry and scaly looking skin, gross decrease in weight, distention in abdomen, loss of muscle mass.
                 
                 c)KWASHIORKOR - It is a malnutrition produced by a severely inadequate amount of protein in the diet. Next 50 entries in dataset denotes KWASHIORKOR i.e     from  id 101 to 150. there will be no apparent decrease in the weight because of edema which adds extra water weight making child looking normal but the effect of malnutrition continously increases which can be accessed by poor appetite, baby feeling lethargic and sleepy all the time,  presence of edema which makes subcutenious fat readings normal. Edema can be accessed by presure on the bony prominences, puffyness of eyes and face which is usually present. Dermatotic changes in skin, organomegaly- gross wasting of muscle mass. Serum  albumin being major contributor in diagnosis usually will be less than 3 gm/L.
PROGRAM :

     Here dataset comes under supervised learning->classification so we use logistic regression to train and test the model. The setwise explanation is given in the program  itself through comments.
REFERENCES:

      1.A special thanks to my brother Dr.Jeevan Y M (Medical Officer at phc Kembalu,Hassan,Karnataka).
      2.Book - Ghai Essential Pediatrics(8th edition) - vinod k paul, arvind bagga.
      3.https://www.medicalnewstoday.com/articles/313185
      4.https://www.geeksforgeeks.org/ml-logistic-regression-using-python/
