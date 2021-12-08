import unittest



def cam_tit (strN):
  n_str= ""
  state = True
  for letter in strN:
    if not letter .isalpha():
      n_str = n_str + letter
      state = True
    else:
      if state:
        n_str = n_str + letter.upper()
        state = False
      else:
        n_str = n_str + letter.lower()

  return n_str

class Pruebas(unittest.TestCase):
    def tests_cam_tit(self):
        self.assertEqual(cam_tit('esto es una frase'), 'Esto Es Una FrasE', 'Error al convertir cadena minuscula')
        self.assertEqual(cam_tit('ESTO ES UNA FRASE'), 'Esto Es Una Frase')


if __name__ == "__main__":
    unittest.main()