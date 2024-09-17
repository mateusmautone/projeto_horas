import unittest
from src.horas_trabalhadas import calcular_horas_trabalhadas

class TestHorasTrabalhadas(unittest.TestCase):

    def test_calculo_horas_trabalhadas(self):
        inicio = "09:00"
        fim = "17:00"
        horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
        self.assertEqual(horas_trabalhadas, 8)
    
    def test_calculo_com_intervalo(self):
        inicio = "09:00"
        fim = "17:00"
        intervalo = "01:00"
        horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim, intervalo)
        self.assertEqual(horas_trabalhadas, 7)

    def test_calculo_horas_invertidas(self):
        inicio = "17:00"
        fim = "09:00"
        horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
        self.assertEqual(horas_trabalhadas, 16)

    def test_calculo_horas_sem_doispontos(self):
        inicio = "0900"
        fim = "1700"
        horas_trabalhadas = calcular_horas_trabalhadas(inicio, fim)
        self.assertEqual(horas_trabalhadas, 8)

if __name__ == "__main__":
    unittest.main()
