def give_blood(b, p):
    treated = min(blood[b], patients[p])
    blood[b] -= treated
    patients[p] -= treated
    return treated


blood = input()
patients = input()

blood = blood.split(" ")
blood = [int(i) for i in blood]

patients = patients.split(" ")
patients = [int(i) for i in patients]

patients_treated = 0

# treat same type and RH
for i in range(8):
    patients_treated += give_blood(i, i)

# Negative RH
# A-
patients_treated += give_blood(0, 2)
# B-
patients_treated += give_blood(0, 4)
# AB-
patients_treated += give_blood(0, 6) + give_blood(2, 6) + give_blood(4, 6)

# Positive RH
# O+ (O-)
patients_treated += give_blood(0, 1)
# A+ (O-, O+, A-)
patients_treated += give_blood(0, 3) + give_blood(1, 3) + give_blood(2, 3)
# B+ (O-, O+, B-)
patients_treated += give_blood(0, 5) + give_blood(1, 5) + give_blood(4, 5)
# AB+ (O-, O+, B-, B+, A-, A+)
for i in range(7):
    patients_treated += give_blood(i, 7)

print(patients_treated)