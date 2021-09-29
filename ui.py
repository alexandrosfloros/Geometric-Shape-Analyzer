import matplotlib.pyplot as plt
from PyQt6.QtWidgets import *
from geometry import *
from random import randrange

class UI(QMainWindow):
    def __init__(self):
        self.tree_updated = True

        super().__init__()
        self.setWindowTitle("Shape Analysis")
        self.setGeometry(0, 0, 600, 400)

        self.main_widget = QWidget(self)
        self.main_layout = QVBoxLayout(self.main_widget)

        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)

        self.input_frame = QFrame(self.main_widget)
        self.input_layout = QGridLayout(self.input_frame)

        self.x_spinbox = QSpinBox(self.input_frame)
        self.x_spinbox.setPrefix("X: ")
        self.x_spinbox.setMinimum(-16)
        self.x_spinbox.setMaximum(16)
        self.input_layout.addWidget(self.x_spinbox, 1, 1, 1, 1)

        self.y_spinbox = QSpinBox(self.input_frame)
        self.y_spinbox.setPrefix("Y: ")
        self.y_spinbox.setMinimum(-16)
        self.y_spinbox.setMaximum(16)
        self.input_layout.addWidget(self.y_spinbox, 2, 1, 1, 1)

        self.add_button = QPushButton(self.input_frame)
        self.add_button.setText("Add")
        self.add_button.clicked.connect(self.spinbox_add_point)
        self.input_layout.addWidget(self.add_button, 1, 2, 1, 1)

        self.remove_button = QPushButton(self.input_frame)
        self.remove_button.setText("Remove")
        self.remove_button.clicked.connect(self.spinbox_remove_point)
        self.input_layout.addWidget(self.remove_button, 2, 2, 1, 1)

        self.clear_button = QPushButton(self.input_frame)
        self.clear_button.setText("Clear")
        self.clear_button.clicked.connect(self.clear_points)
        self.input_layout.addWidget(self.clear_button, 2, 3, 1, 1)

        self.calculate_button = QPushButton(self.input_frame)
        self.calculate_button.setText("Find\nShapes")
        self.calculate_button.clicked.connect(self.calculate)
        self.input_layout.addWidget(self.calculate_button, 3, 1, 1, 3)

        self.random_frame = QFrame(self.input_frame)
        self.random_layout = QHBoxLayout(self.random_frame)
        self.random_layout.setContentsMargins(0, 0, 0, 0)

        self.random_button = QPushButton(self.random_frame)
        self.random_button.setText("Random")
        self.random_button.clicked.connect(self.random_points)
        self.random_layout.addWidget(self.random_button)

        self.random_spinbox = QSpinBox(self.random_frame)
        self.random_spinbox.setMinimum(1)
        self.random_spinbox.setMaximum(10)
        self.random_layout.addWidget(self.random_spinbox)

        self.input_layout.addWidget(self.random_frame, 1, 3, 1, 1)
        self.main_layout.addWidget(self.input_frame)

        self.plot_frame = QFrame(self.main_widget)
        self.plot_layout = QHBoxLayout(self.plot_frame)

        self.plot_table = QTableWidget(self.plot_frame)
        self.plot_table.setColumnCount(2)
        self.plot_table.horizontalHeader().setStretchLastSection(True)
        self.plot_table.setHorizontalHeaderLabels(["X","Y"])
        self.plot_table_delegate = ReadOnlyDelegate(self.plot_table)
        self.plot_table.setItemDelegateForColumn(0, self.plot_table_delegate)
        self.plot_table.setItemDelegateForColumn(1, self.plot_table_delegate)

        self.plot_tree = QTreeWidget(self.plot_frame)
        self.plot_tree.setColumnCount(1)
        self.plot_tree.setHeaderLabel("No shapes found - At least 3 points are needed!")
        self.plot_tree.currentItemChanged.connect(self.click_points_item)

        self.plot_layout.addWidget(self.plot_table)
        self.plot_layout.addWidget(self.plot_tree)
        self.main_layout.addWidget(self.plot_frame)
    
    def get_point(self):
        point = np.array([self.x_spinbox.value(), self.y_spinbox.value()])
        return point

    def spinbox_add_point(self):
        point = self.get_point()
        if not any(np.array_equal(p, point) for p in point_list):
            self.add_point(point)
    
    def spinbox_remove_point(self):
        point = self.get_point()
        if any(np.array_equal(p, point) for p in point_list):
            self.remove_point(point)

    def add_point(self, point):
            point_list.append(point)
            self.update_points()

    def remove_point(self, point):
        global point_list
        new_point_list = []
        for p in point_list:
            if not np.array_equal(p, point):  
                new_point_list.append(p)
        point_list = new_point_list.copy()
        self.update_points()
    
    def random_points(self):
        point_num = self.random_spinbox.value()
        for i in range(point_num):
            self.add_random()
        self.update_points()

    def add_random(self):
        x = randrange(-16, 17)
        y = randrange(-16, 17)
        point = np.array([x, y])
        if any(np.array_equal(p, point) for p in point_list):
            self.add_random()
        else:
            point_list.append(point)

    def clear_points(self):
        point_list.clear()
        self.update_points()
        self.x_spinbox.setValue(0)
        self.y_spinbox.setValue(0)
        self.random_spinbox.setValue(1)

    def create_plot(self):
        self.fig, self.axes = plt.subplots()
        self.set_axes()
        self.fig.canvas.mpl_connect("button_press_event", self.click_plot)
        plt.gca().set_aspect("equal", adjustable = "box")
    
    def set_axes(self):
        self.axes.set_title("Left click to add or remove a point")
        self.axes.set_xlim(-16, 16)
        self.axes.set_ylim(-16, 16)
        self.axes.set_xticks(np.arange(-16, 17), minor = True)
        self.axes.set_yticks(np.arange(-16, 17), minor = True)
        self.axes.grid(which= "major", alpha = 0.6)
        self.axes.grid(which= "minor", alpha = 0.3)
    
    def update_points(self):
        self.tree_updated = False
        if len(point_list) < 3:
            self.plot_tree_message("few_points")
        else:
            self.plot_tree_message("outdated")
        self.plot_tree.clear()
        self.update_table()
        self.update_plot()

    def update_table(self):
        self.plot_table.setRowCount(len(point_list))

        for n, p in enumerate(point_list):
            self.plot_table.setItem(n, 0, QTableWidgetItem(str(p[0])))
            self.plot_table.setItem(n, 1, QTableWidgetItem(str(p[1])))

    def update_tree(self, shapes):
        self.plot_tree.clear()
        if shapes.parallelograms:
            shape_item = self.get_shape_item(shapes.parallelograms, "parallelograms")
            points_items = self.get_points_items(shapes.parallelograms)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        if shapes.rectangles:
            shape_item = self.get_shape_item(shapes.rectangles, "rectangles")
            points_items = self.get_points_items(shapes.rectangles)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        if shapes.rhombi:
            shape_item = self.get_shape_item(shapes.rhombi, "rhombi")
            points_items = self.get_points_items(shapes.rhombi)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        if shapes.squares:
            shape_item = self.get_shape_item(shapes.squares, "squares")
            points_items = self.get_points_items(shapes.squares)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        if shapes.isosceles_trapezia:
            shape_item = self.get_shape_item(shapes.isosceles_trapezia, "isosceles_trapezia")
            points_items = self.get_points_items(shapes.isosceles_trapezia)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        if shapes.isosceles_triangles:
            shape_item = self.get_shape_item(shapes.isosceles_triangles, "isosceles_triangles")
            points_items = self.get_points_items(shapes.isosceles_triangles)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        if shapes.right_triangles:
            shape_item = self.get_shape_item(shapes.right_triangles, "right_triangles")
            points_items = self.get_points_items(shapes.right_triangles)
            shape_item.addChildren(points_items)
            self.plot_tree.addTopLevelItem(shape_item)
        
        if len(shapes.parallelograms) == 0 and len(shapes.isosceles_trapezia) == 0 and len(shapes.isosceles_triangles) == 0 and len(shapes.right_triangles) == 0:
            self.plot_tree_message("no_shapes")
            return

        self.plot_tree_message("shapes_found")
    
    def get_shape_item(self, shape, name):
        item = QTreeWidgetItem(self.plot_tree)
        text = name + f"({len(shape)})"
        item.setText(0, text)
        return item
    
    def get_points_items(self, shape):
        items = []
        if isinstance(shape[0], Quadrilateral):
            for s in shape:
                items.append(QTreeWidgetItem([f"{s.point1}, {s.point2}, {s.point3}, {s.point4}"]))
        else:
            for s in shape:
                items.append(QTreeWidgetItem([f"{s.point1}, {s.point2}, {s.point3}"]))
        return items


    def update_plot(self):
        if not plt.fignum_exists(1):
            self.create_plot()
        plt.cla()
        self.set_axes()

        for p in point_list:
            self.axes.plot(p[0], p[1], marker = "o", markersize = 3, color = "blue")
        
        plt.show()

    def click_plot(self, event):
        try:
            x, y = int(round(event.xdata)), int(round(event.ydata))
            point = np.array([x, y])
            if any(np.array_equal(p, point) for p in point_list):
                self.remove_point(point)
            else:
                self.add_point(point)
            self.x_spinbox.setValue(x)
            self.y_spinbox.setValue(y)
        except:
            pass

    def click_points_item(self, item):
        self.update_plot()
        try:
            text = item.text(0)
            if " " in text:
                points = text.split(", ")

                for n, p in enumerate(points):
                    p = p.replace("[", "").replace("]", "")
                    x, y = p.split()
                    points[n] = np.array([int(x), int(y)])

                self.axes.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], marker = "o", markersize = 3, color = "red")
                self.axes.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], marker = "o", markersize = 3, color = "red")
                if len(points) == 3:
                    self.axes.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], marker = "o", markersize = 3, color = "red")
                else:
                    self.axes.plot([points[2][0], points[3][0]], [points[2][1], points[3][1]], marker = "o", markersize = 3, color = "red")
                    self.axes.plot([points[3][0], points[0][0]], [points[3][1], points[0][1]], marker = "o", markersize = 3, color = "red")
        except:
            pass

    def calculate(self):
        if not self.tree_updated:
            if len(point_list) > 2:
                self.tree_updated = True
                shapes = calculate(point_list)
                self.update_tree(shapes)
            else:
                self.plot_tree_message("few_points")

    def plot_tree_message(self, id):
        if id == "few_points":
            self.plot_tree.setHeaderLabel("No shapes found - At least 3 points are needed!")
        elif id == "outdated":
            self.plot_tree.setHeaderLabel("Outdated - Press Find Shapes to update!")
        elif id == "no_shapes":
            self.plot_tree.setHeaderLabel("No shapes found - Try adding more points!")
        elif id == "found_shapes":
            self.plot_tree.setHeaderLabel("Shapes:")

class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return