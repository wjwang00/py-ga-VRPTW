import json
import os
import matplotlib.pyplot as plt
from gavrptw import BASE_DIR

json_data_dir = os.path.join(BASE_DIR, 'data', 'json', 'R101.json')

# 从JSON文件加载数据
with open(json_data_dir, 'r') as json_file:
    data = json.load(json_file)

# 提取depart坐标
depart_x = data['depart']['coordinates']['x']
depart_y = data['depart']['coordinates']['y']

# 提取customer_i的坐标
x_coordinates = []
y_coordinates = []

for customer_key, customer_data in data.items():
    if customer_key != 'depart' and customer_key.startswith('customer_'):
        x_coordinates.append(customer_data['coordinates']['x'])
        y_coordinates.append(customer_data['coordinates']['y'])

# 定义路径列表
routes = [[4, 21, 23, 22, 18, 19], [2, 16, 13, 12, 25], [9, 8, 14, 15, 6], [17, 5, 3, 20, 1], [24, 10, 11, 7]]

# 绘制散点图
plt.scatter(x_coordinates, y_coordinates, label='Customers')
plt.scatter(depart_x, depart_y, color='red', marker='D', s=100, label='Depart')

# 绘制路径
for route in routes:
    route_x = [depart_x] + [data[f'customer_{customer_id}']['coordinates']['x'] for customer_id in route] + [depart_x]
    route_y = [depart_y] + [data[f'customer_{customer_id}']['coordinates']['y'] for customer_id in route] + [depart_y]
    plt.plot(route_x, route_y, marker='o', markersize=5)

# 标记"depart"标签
plt.text(depart_x, depart_y, 'Depart', fontsize=12, verticalalignment='bottom')

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Customer and Depart Locations with Routes')
plt.legend()
plt.grid(True)
plt.show()
