# Pyfun Workshop 4

## Introduction

Before we start entering today's topic, let's have a small revision about OOP.

### Some slight Basic Revision on OOP in Python

OOP stands for Object Oriented Programming, and it is a programming paradigm based around the concept of "objects".

Programming paradigm here refers to the approach, pattern, style,"way" of programming, as each programming language have a set of paradigm that they support and are designed with it in mind.

Python is a multi-paradigm language, but here we will just be using some OOP for GUI programming with Kivy.

So what is OOP then? What does it mean to be "object-oriented" ?

In very simple terms, object-oriented programming refers to the paradigm of programming that models and group code together by modelling them as objects. Each object can have their own fields, attributes (variables) and methods(function).

Take this code for example:

```python
# Class is like a blueprint
# so in this case we can say that the car class is a blueprint,
# and I can use this blueprint(class) to create a car object.
class Car:
    def __init__(self):
        self.speed = 50

    def move(self):
        print(f"moving at {self.speed}")

car = Car() # create a new object from the class
car.move() # prints out "Moving at 50"
```

We create a car class, which is basically a blueprint for creating car objects. In the class we can see that there is two functions, but we don't call them functions if they are in a class, we call them **methods**. The `__init__` method is an initialization method which will be called when we are creating the object. `self.speed` is a **field** that the Car Object have, initialized in the `__init__` method. The `move` methods is modeled after something cars does, which is moving :p, but here it won't actually move anything but just print out how fast it is moving.

We later see the line `car = Car()` which is actually the moment where a car object is created from the class. The created `car` object would have all the fields and methods defined in the class. Thus, the next line, when we call `car.move()`, the program will print out the line "Moving at 50".

### Graphical User Interface

Graphical user interface, or GUI, is a form of user interface that allows user to interact through a graphical icons and visual indicators instead of text-based user interface.

It is something created with user experience in mind, to allow users to easily interact with computers, as terminal commands have a high learning curve for users (remembering commands on terminals are hard!).

Your laptop, your browser, and most of the things you see on your computer screen now are GUI instead of the text basied user interface.

People used to work with this when they wanted to use the computer:

![Terminal](https://cdn-images-1.medium.com/max/1600/1*wYbd8RilLewHffJY_Hqs6w.gif)

Gradually GUI like these were developed:

![SmallTalk GUI](https://upload.wikimedia.org/wikipedia/commons/9/91/Smalltalk-76.png)

And now we have this!

![windows 10](https://i0.wp.com/thetechhacker.com/wp-content/uploads/2017/01/What-is-GUI-Graphical-user-Interface.jpg?fit=1000%2C640&ssl=1)

### Enter Kivy

[Kivy](https://kivy.org/doc/stable/) is a open source python library for app development. According to its official website:
> Kivy is a Open source python library for rapid development of applications that make use of innovative user interface, such as multi-touch apps.

It is also cross platform, meaning that you can run it on Windows, Mac, Linux, Android, IOS and also RasberryPI.

For today's project, we will be mainly using Kivy(if you haven't notice yet), instead of the built in library tkinter.

## Requirements and Dependencies

- Python 3.7
- Kivy and its dependencies

**For windows user, simply do :**

```bash
pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew kivy
```

**For mac and linux users, please refer to the official guide at kivy's official documentation.**

[Mac Guide](https://kivy.org/doc/stable/installation/installation-osx.html)

[Linux Guide](https://kivy.org/doc/stable/installation/installation-linux.html)

## Creating a Desktop App using Python

After installing all the requirements and dependencies, let us start on creating a desktop application!

### Creating our first ever Kivy application

Let's start with a simple hello world app like we always do.

Start with importing App from kivy and extending it for our application class.

```python
from kivy.app import App

class MyApp(App):
    pass
```

What we did is just importing the App class from kivy, which is the base for most kivy application.
We then **extend** this class to create our **own** version of Application. By extending the App class, we can customize our application's behaviour to our liking, via overriding some methods given to us.

Before that, let's try running the app using the run method. Simply add `MyApp().run()` run your gui.

```python
from kivy.app import App

class MyApp(App):
    pass

MyApp().run()
```

Run it with `python {your_filename}.py`.
You should see a blank black window popping up.

Let's try adding our first widget to it! Import the Label widget from kivy.

```python
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    pass

MyApp().run()
```

Now let's add and display the widget in our app. To do that, we must override the `build` method for our app.

```python
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text="Hello World")

MyApp().run()
```

Try running the application now, you should still see a black screen, but now there should be "Hello World" written in the middle of the window.

As the `build` method will be called by the kivy application when it is initializing, by adding `return Label(text="Hello World")` to the `build` method, we are telling kivy to initialize the Label with the sentence "Hello world" on it, and set it as our root Widget, as the first Widget returned by the build method will automatically be set as root widget. Here root widget refers to the outer most widget.

But wait a second, what are widgets? Widgets in Kivy are the basic building blocks for GUI interfaces in kivy. They are essentially components and parts that make up an applications. According to the official kivy widgets documentation,
> A Widget is the base building block of GUI interfaces in Kivy. It provides a Canvas that can be used to draw on screen. It receives events and reacts to them.

Things like button, label, textbox and dropdown are all considered widgets by kivy. You can either use kivy's widget to build your application, or if you need it, combine or extend them to create your own customized widget!

### Why not create the best "game" of our childhood?

By that title I meant a painting app, just in case you didn't get it :)

This tutorial is taken from the official tutorial from [here](https://kivy.org/doc/stable/tutorials/firstwidget.html#).

Let's start with what we learnt earlier, with some name changes.

```python
from kivy.app import App

class MyPaintApp(App):
    def build(self):
        pass

MyPaintApp().run()
```

Let's create our first customized widget, The MyPaintWidget, that provides us with the painting functionality.

```python
from kivy.app import App
from kivy.uix.widget import Widget

class MyPaintWidget(Widget):
    pass

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

MyPaintApp().run()
```

Here we extend the base Widget class and for our MyPaintWidget to obtain all the basic functionalities of a Widget in Kivy after importing it. We then return an instance(object) of the MyPaintWidget at the `build` function in MyPaintApp, which if you remember, will initialise the Application with a MyPaintWidget object and use it as the root widget, causing it to occupy the entire screen.

Before we continue, let's talk about how widgets are arranged and their hierachies. Widget in Kivy is organized in trees, there is a root widget, and it has children of its own which are also widgets. The chidren can also have its own widgets, and so on.

![widget](https://kivy.readthedocs.io/en/master/_images/pos_hint.jpg)

Let's try to add some behaviour to our first Widget!

```python
from kivy.app import App
from kivy.uix.widget import Widget

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print(touch)

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

MyPaintApp().run()
```

Now if you run the application again, you will see that it prints out the coordinate where you clicked on the application.

When you add the function `on_touch_down` into MyPaintWidget, you were essentially telling kivy what to do when you clicked on the widget, which in this case, is printing out the mouse motion event that contains information such as the x and y coordinates for your click.

There are also other types of motion events that we can handle and implement, such as `on_touch_up` and `on_touch_move`, which we will use later.

```python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,1,0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

MyPaintApp().run()
```

Now, we added the functionality to draw a circle when we clicked our paint widget. We first initialise the color we use using the `Color()` object, then we draw a ellipse with a diameter of 30.0, which will be in the Color that we have set.

Let's continue on and add the functionality to draw a line when we hold down the click!

```python
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,1,0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()

MyPaintApp().run()
```

Run the code now and you should be able to draw a line if you hold your mouse down in addition to the circle.

What we added in the code above is the line `touch.ud['line'] = Line(points=(touch.x, touch.y))` which creates a Line object with a starting coordinates and save it into the `touch.ud['line']` dictionary. We then implement the `on_touch_move`, and access the saved Line object via `touch.ud['line']`, and add more points to the Line as long as we keep our mouse down.

At this point, the paint app can be considered done. However, you'll realise soon then there is no way to clear the screen without restarting the application, so why not implement that too?

```python
from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random())
            d = 30.
            Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d, d))
            touch.ud['line'] = Line(points=[touch.x, touch.y])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget()
        clear_btn = Button(text="Clear")
        clear_btn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clear_btn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

MyPaintApp().run()
```

Here you can see we made some changes to the `build` function. We used a base Widget as the root widget and added MyPaintWidget as its child. We then add a Button to the root widget that will function as a clear button. Finally, we change the code to return the root node instead of MyPaintWidget. 

Implementing the clear function is just as easy and just require us to clear the canvas by calling the `clear()` function on the MyPaintWidget which can be accessed by `self.painter.canvas` via our definition. Make sure you bind the button with the clear function and now you should now be able to clear the screen using the clear button.

Just for more fun with this application, I also used the random function to randomise the color I get when drawing simple by replacing the constant value in `Color` to `random()`, which will generate a random decimal number for me within 0 and 1.

And here you have it! Your simple paint application created from python with Kivy!

Feel free to try to create your own application by using what you've learnt here!