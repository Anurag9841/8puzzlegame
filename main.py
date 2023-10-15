import matplotlib.pyplot as plt
import matplotlib.image as img
from Nodes import Node
from bfs import breadthfirstsearch
initial_state= [3,3,0]
Node.i=0
solution=breadthfirstsearch(initial_state)
print('Solution:', solution)
print('space:',Node.i)
image_paths = ['Final_solution0.png', 'Final_solution1.png','Final_solution2.png','Final_solution3.png','Final_solution4.png','Final_solution5.png','Final_solution6.png','Final_solution7.png','Final_solution8.png','Final_solution9.png','Final_solution10.png']


for i, image_path in enumerate(image_paths):
    image = img.imread(image_path)
    plt.imshow(image)
    plt.title(f'Image {i + 1}')
    plt.waitforbuttonpress()
plt.close('all')



