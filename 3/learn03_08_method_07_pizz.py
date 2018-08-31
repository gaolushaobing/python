import learn03_08_method_07_pizz_model
learn03_08_method_07_pizz_model.make_pizza(16, 'pep')
learn03_08_method_07_pizz_model.make_pizza(12, 'extra butter', 'cheese')

from learn03_08_method_07_pizz_model import make_pizza
make_pizza(21, 'Nothing', 'Nothing, Nothing')

from learn03_08_method_07_pizz_model import make_pizza as m
m(19, 'a', 'b', 'c')