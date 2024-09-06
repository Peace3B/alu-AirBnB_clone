*PROJECT DESCRIPTION.*

This project is the initial step towards building a full web application, the Airbnb clone. The goal is to create a command interpreter (also known as a console) to manage Airbnb objects. This console will allow you to create, update, delete, and manage various objects (like Users, Places, etc.) that are necessary for the application's backend. It has two authors namely Peace KEZA and NTWALI Eliel.

*STEP 1 : THE CONSOLE.*

*Command Interpreter Description.*

The command interpreter is a custom-built shell that enables users to manage the Airbnb objects through various commands. It performs the following functions:

* Create new objects (like a new User or Place).

* Retrieve objects from storage (file or database).

* Perform operations on objects (such as counting or computing statistics).

* Update object attributes.

* Destroy objects.

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

*Relevant Files And Directories*

* models: directory will contain all classes used for the entire project. A class, called “model” in a OOP * project is the representation of an object/instance.

* tests: directory will contain all unit tests.

* console.py: file is the entry point of our command interpreter.

* models/base_model.py: file is the base class of all our models. It contains common elements: .attributes: id, created_at and updated_at .methods: save() and to_json()

* models/engine: directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

*Using The Console*

* Run the console: ./console.py

* Quit the console: (hbnb) quit

* Display the help for a command: (hbnb) help

* Show an object: (hbnb) show or (hbnb) .show()

* Destroy an object: (hbnb) destroy or (hbnb) .destroy()

* Show all objects, or all instances of a class: (hbnb) all or (hbnb) all

* Update an attribute of an object: (hbnb) update "" or (hbnb) .update(, , "")

*Examples;*

*Interactive Mode:*

$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
===================================
EOF  help  quit

(hbnb) 

(hbnb)
 
(hbnb) quit

$



*Non-Interactive Mode:*

$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
==================================

EOF  help  quit

(hbnb) 

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)

Documented commands (type help <topic>):
==================================

EOF  help  quit

(hbnb) 

$



*AUTHORS.*
* PEACE KEZA
* NTWALI Eliel

