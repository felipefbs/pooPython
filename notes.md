Definição simples de uma classe.

```python
class MyClass:
    def __init__(self, attribute):
        self.myAtribute = "Atribute"
        self.myOtherAtribute = atribute
    
    def myMethod(self): # Precisa do self para fazer o acesso externo desse método
        print("Method 1", self.myAtribute)

    def myMethod2(self, num: int, mult:int) -> int:   # Precisa do self para fazer o acesso externo desse método
        return num * mult

ob = MyClass("An atribute")
ob.MyMethod()
ob.MyMethod(2, 3)
```