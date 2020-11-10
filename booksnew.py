#importamos la librería para trabajar con xml
import xml.etree.ElementTree as ET

#Se le va a signar a tree un objeto, por el uso de la librería y el parse
#sobre el archivo xml
tree = ET.parse('books.xml')
print(tree)

#Ahora quiero ir a la raíz de mi xml
root = tree.getroot()
print(root)

#Ahora quiero hacer cosas con esto, lo puedo tratar como una colección.
#Debería traer el tag con el índice cero <children>, porque la raíz
#es <books>
print(root[0].tag)

#Ahora quiero que traiga el tag del índice cero <children> y dentro de ese tag
#el índice cero <title>, porque la raíz es <books>
print(root[0][0].tag)

#Ahora quiero que traiga el texto del índice cero <children> y dentro de ese tag
#el índice 0 <title>, porque la raíz es <books>
print(root[0][0].text)

#Utilizando cadenas
print('Para el ' + root[0][0].tag + ' tenemos el valor ' + root[0][0].text)

#Recuperar los hijos del root y mostrarlos
children = root.getchildren()
#La variable child va a recorrer todos los elementos que tenga children,
#posteriormente de los elementos encontrados va a mostrar el tag
#va a mostrar los hijos del root, los cuales son children y programming
for child in children:
    print(child.tag)
    #Ahora quiero los hijos de child y mostrarlos
    items = child.getchildren()
    #La variable item va a recorrer todos los elementos que tenga items,
    #posteriormente de los elementos encontrados va a mostrar el tag
    #va a mostrar los hijos de cada child.
    for item in items:
        print(item.tag)
        #También podemos agregar que nos muestre el texto de los hijos del hijo.
        #Va a presentar tag + texto
        print(item.text)
