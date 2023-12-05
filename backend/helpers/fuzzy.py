import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Tạo biến đầu vào thể lực
fitness = ctrl.Antecedent(np.arange(10, 50, 1), 'fitness')
eyesight = ctrl.Antecedent(np.arange(0, 20, 1), 'eyesight')
tooth_loss = ctrl.Antecedent(np.arange(0, 28, 1), 'tooth_loss')
heart_rate = ctrl.Antecedent(np.arange(50, 150, 1), 'heart_rate')
hearing_capacity = ctrl.Antecedent(np.arange(0, 20, 1), 'hearing_capacity')
muscle_cramp = ctrl.Antecedent(np.arange(0, 6, 1), 'muscle_cramp')
health = ctrl.Consequent(np.arange(1, 7, 1), 'health')

fitness['1'] = fuzz.trapmf(fitness.universe, [18, 18, 24, 25])
fitness['2'] = fuzz.trapmf(fitness.universe, [24, 25, 26, 27])
fitness['3'] = fuzz.trapmf(fitness.universe, [26, 27, 29, 30])
fitness['4'] = fuzz.trapmf(fitness.universe, [29, 30, 35, 35])
fitness['5'] = fuzz.trapmf(fitness.universe, [35, 35, 39, 40])
fitness['6'] = fuzz.trapmf(fitness.universe, [39, 40, 50, 50])

eyesight['1'] = fuzz.trapmf(eyesight.universe, [18, 19, 20, 20])
eyesight['2'] = fuzz.trimf(eyesight.universe, [17, 18, 19])
eyesight['3'] = fuzz.trimf(eyesight.universe, [16, 17, 18])
eyesight['4'] = fuzz.trimf(eyesight.universe, [15, 16, 17])
eyesight['5'] = fuzz.trimf(eyesight.universe, [13, 14, 15])
eyesight['6'] = fuzz.trapmf(eyesight.universe, [0, 0, 12, 13])

tooth_loss['1'] = fuzz.trimf(tooth_loss.universe, [0, 0, 0])
tooth_loss['2'] = fuzz.trapmf(tooth_loss.universe, [0, 1, 3, 4])
tooth_loss['3'] = fuzz.trapmf(tooth_loss.universe, [2, 3, 5, 6])
tooth_loss['4'] = fuzz.trapmf(tooth_loss.universe, [4, 5, 7, 8])
tooth_loss['5'] = fuzz.trapmf(tooth_loss.universe, [6, 7, 28, 28])

heart_rate['1'] = fuzz.trimf(heart_rate.universe, [55, 70, 85])
heart_rate['2'] = fuzz.trimf(heart_rate.universe, [80, 87, 95])
heart_rate['3'] = fuzz.trimf(heart_rate.universe, [90, 95, 105])
heart_rate['4'] = fuzz.trimf(heart_rate.universe, [100, 107, 115])
heart_rate['5'] = fuzz.trimf(heart_rate.universe, [110, 115, 120])
heart_rate['6'] = fuzz.trapmf(heart_rate.universe, [115, 120, 150, 150])

hearing_capacity['1'] = fuzz.trapmf(hearing_capacity.universe, [10, 10, 20, 20])
hearing_capacity['2'] = fuzz.trapmf(hearing_capacity.universe, [5, 6, 8, 10])
hearing_capacity['3'] = fuzz.trapmf(hearing_capacity.universe, [3, 4, 6, 7])
hearing_capacity['4'] = fuzz.trapmf(hearing_capacity.universe, [2, 3, 4, 5])
hearing_capacity['5'] = fuzz.trapmf(hearing_capacity.universe, [1, 1.5, 2, 3])
hearing_capacity['6'] = fuzz.trapmf(hearing_capacity.universe, [0, 0, 1, 1.5])

muscle_cramp['1'] = fuzz.trimf(muscle_cramp.universe, [0, 0, 0])
muscle_cramp['5'] = fuzz.trimf(muscle_cramp.universe, [1, 1, 3])
muscle_cramp['6'] = fuzz.trimf(muscle_cramp.universe, [3, 5, 5])

health['1'] = fuzz.trimf(health.universe, [1, 1, 1])
health['2'] = fuzz.trimf(health.universe, [2, 2, 2])
health['3'] = fuzz.trimf(health.universe, [3, 3, 3])
health['4'] = fuzz.trimf(health.universe, [4, 4, 4])
health['5'] = fuzz.trimf(health.universe, [5, 5, 5])
health['6'] = fuzz.trimf(health.universe, [6, 6, 6])

# Xem hàm thành viên
# eyesight.view()
# tooth_loss.view()
# heart_rate.view()
# hearing_capacity.view()
# muscle_cramp.view()
# health.view()


rule1 = ctrl.Rule(fitness['1'] & eyesight['1'] & tooth_loss['1'] & heart_rate['1'] & hearing_capacity['1'] & muscle_cramp['1'], health['1'])
rule2 = ctrl.Rule((fitness['2'] | eyesight['2'] | tooth_loss['2'] | heart_rate['2'] | hearing_capacity['2']) & muscle_cramp['1'], health['2'])
rule3 = ctrl.Rule((fitness['3'] | eyesight['3'] | tooth_loss['3'] | heart_rate['3'] | hearing_capacity['3']) & muscle_cramp['1'], health['3'])
rule4 = ctrl.Rule((fitness['4'] | eyesight['4'] | tooth_loss['4'] | heart_rate['4'] | hearing_capacity['4']) & muscle_cramp['1'], health['4'])
rule5 = ctrl.Rule(fitness['5'] | eyesight['5'] | tooth_loss['5'] | heart_rate['5'] | hearing_capacity['5'] | muscle_cramp['5'], health['5'])
rule6 = ctrl.Rule(fitness['6'] | eyesight['6'] | heart_rate['6'] | hearing_capacity['6'] | muscle_cramp['6'], health['6'])

health_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
health_system = ctrl.ControlSystemSimulation(health_ctrl)

def fuzzy(
    chieu_cao: float,
    can_nang: float,
    mat: float,
    rang: float,
    suc_nghe: float,
    mach: float,
    co_rut: float
  ):

  input_fitness = can_nang/pow(chieu_cao/100, 2)
  print(input_fitness)
  # Gán giá trị cho các biến đầu vào
  health_system.input['fitness'] = input_fitness
  health_system.input['eyesight'] = mat
  health_system.input['tooth_loss'] = rang
  health_system.input['heart_rate'] = mach
  health_system.input['hearing_capacity'] = suc_nghe
  health_system.input['muscle_cramp'] = co_rut

  # Chạy hệ thống fuzzy
  health_system.compute()

  # Lấy giá trị đầu ra
  predicted_health = health_system.output['health']

  point1=fuzz.interp_membership(health.universe, health['1'].mf, health_system.output['health'])
  point2=fuzz.interp_membership(health.universe, health['2'].mf, health_system.output['health'])
  point3=fuzz.interp_membership(health.universe, health['3'].mf, health_system.output['health'])
  point4=fuzz.interp_membership(health.universe, health['4'].mf, health_system.output['health'])
  point5=fuzz.interp_membership(health.universe, health['5'].mf, health_system.output['health'])
  point6=fuzz.interp_membership(health.universe, health['6'].mf, health_system.output['health'])
  return point1, point2, point3, point4, point5, point6
  