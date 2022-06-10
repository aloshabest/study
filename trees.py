# Требуется реализовать программу по работе с решающими деревьями:
# Здесь в каждом узле дерева делается проверка (задается вопрос). Если проверка проходит, то осуществляется переход к следующему объекту по левой стрелке (с единицей), а иначе - по правой стрелке (с нулем). И так до тех пор, пока не дойдем до одного из листа дерева (вершины без потомков).
#
# В качестве входных данных будет использоваться вектор (список) с бинарными значениями: 1 - да, 0 - нет. Каждый элемент этого списка соответствует своему вопросу.
# Для реализации решающих деревьев в программе следует объявить два класса:
#
# TreeObj - для описания вершин и листьев решающего дерева;
# DecisionTree - для работы с решающим деревом в целом.
#
# В классе DecisionTree должны быть реализованы (по крайне мере) два метода уровня класса (@classmethod):
#
# def predict(cls, root, x) - для построения прогноза (прохода по решающему дереву) для вектора x из корневого узла дерева root.
# def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево;
#
# В методе add_obj параметры имеют, следующие значения:
#
# obj - ссылка на новый (добавляемый) объект решающего дерева;
# node - ссылка на объект дерева, к которому присоединяется вершина obj;
# left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj (True - к левой ветви; False - к правой).
#
# В классе TreeObj следует объявить инициализатор:
#
# def __init__(self, indx, value=None): ...
#
# где indx - проверяемый в вершине дерева индекс вектора x; value - значение, хранящееся в вершине (для промежуточных вершин None).
#
# При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться следующие локальные атрибуты:
#
# indx - проверяемый индекс (целое число);
# value - значение с данными (строка);
# __left - ссылка на следующий объект дерева по левой ветви (изначально None);
# __right - ссылка на следующий объект дерева по правой ветви (изначально None).
#
# Для работы с локальными приватными атрибутами __left и __right необходимо объявить объекты-свойства с именами left и right.
#
# Эти классы в дальнейшем предполагается использовать, следующим образом (эти строчки в программе не писать):
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # будет программистом

class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new):
        self.__left = new

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new):
        self.__right = new


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        indx = 0
        while root.indx != -1:
            if x[indx]:
                root = root.left
                indx = 1
            else:
                root = root.right
                indx = 2
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

root = DecisionTree.add_obj(TreeObj(0))

v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)


