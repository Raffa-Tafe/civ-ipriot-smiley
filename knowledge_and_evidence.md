<style>

body {
    counter-reset: h2counter;
}

/* H1 - No numbering */
h1 {
    /* No counter reset or increment */
}

/* H2 - Level 1 numbering */
h2 {
    counter-reset: h3counter;
}

h2::before {
    counter-increment: h2counter;
    content: counter(h2counter) ". ";
}

/* H3 - Level 2 numbering */
h3 {
    counter-reset: h4counter;
}

h3::before {
    counter-increment: h3counter;
    content: counter(h2counter) "." counter(h3counter) " ";
}

/* H4 - Level 3 numbering (optional) */
h4 {
    counter-reset: h5counter;
}

h4::before {
    counter-increment: h4counter;
    content: counter(h2counter) "." counter(h3counter) "." counter(h4counter) " ";
}

</style>

# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## Required evidence

### Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Run_main.py.png](Run_main.py.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name               | value                          |
   | ----------              |--------------------|--------------------------------|
   | built-in primitive type | tuple="WHITE"      | (255,255,255)                  |
   | built-in composite type | list= "Self.pixel" | list                           |
   | user-defined type       | class Smiley       | the whole program of Smiley.py |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                                            |
   | ------------             |-------------------------------------------------|
   | self.pixels              | Built-in composite type: list                   |
   | A member of self.pixels  | the member inside list "self.pixel" is a: tuple |
   | self                     | instance of the Smiley Class                    |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File      | First line | Line range |
   | ------------ |-----------| -------- |------------|
   |  sequence    | sad.py    | "def draw_mouth(self):"         | 11-18      |
   |  selection   | smiley.py | "def dim_display(self, dimmed=True):"| 58-66      |
   |  iteration   | sad.py    | "for pixel in mouth:"         | 16-18      |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used?                                               | Example |
   | ----------------------- |-----------------------------------------------------| -------|
   | int                     | The inside of an array is int (happy.py)            | "mouth = [41, 46, 50, 51, 52, 53]"       |
   | float                   | The float is used for the delay  (happy.py)         | "def blink(self, delay=0.25):"       |
   | str                     | The class is made with a string variable (happy.py) | "class Happy(Smiley, Blinkable):"       |
   | bool                    | Draw open or closed eyes on a smiley  (happy.py)    | "def draw_eyes(self, wide_open=True):"       |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> "YELLOW" is a class variable. The "YELLOW" class is used for the whole code. Example: After we put the class "YELLOW" they put the class in "Y = self.YELLOW". "SenseHat()" is an instance variable, where you use it once.  
>

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > Constructor is used to initialize the object's properties and set up any necessary state when the object is created. in happy.py, constructor is used to make the smile face by calling the parent constructor and then customizing the mouth and eyes to look happy 
   >

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > "def __init__(self):
    super().__init__()
    self.draw_mouth()
    self.draw_eyes()"
   > The result of these statements is that when a Happy instance is created, it starts with the smiley face attributes and setup defined in Smiley, and then customizes the mouth and eyes to give the face a happy expression.
   

### Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:
   
> It’s likely that PEP8 and Sense HAT’s library code follows similar coding standards to maintain readability and consistency.
>

2. List three aspects of this convention you see applied in the code.

> - Naming Convention: Classes like Smiley and methods like draw_mouth() and dim_display() use lowercase_with_underscores
> - Consistent Converntion: All indentation uses 4 spaces, with consistent block structures and spacing between methods.
> - Docstrings for Method: Most functions and methods include triple-quoted """docstrings""" describing what the method does

3. Give two examples of organizational documentation in the code.

> - """
Draws the mouth feature on a happy face.
"""
> - """
Set the SenseHat's light intensity to low (True) or high (False).
"""
>

### Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s)  |
|------------|---------------|-------------------|
| Smiley     | super         | object            |
| sad        | sub           | Smiley            |
| Blinkable  | super         | abc.ABC           |
| Happy      | sub           | Smiley, Blinkable |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Abstraction has a crucial impact on object-oriented programming. It conceals intricate details and displays the necessary features of an object. This allows individuals to use objects at a higher level without understanding the internal mechanisms. 
The Smiley class in the project demonstrates abstraction in practice. It provides a simple method to display a smiley face on the Sense HAT's LED matrix through its show function. It doesn't expose how it manages pixels or operates the LED matrix. Users of the Smiley class can create and show smiley faces without effort. They don't need to understand pixel operations or how the Sense HAT communicates with the hardware. Instead, they can concentrate on the main functions. This division of responsibilities makes the code more readable and maintainable.



3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> The process of deriving from base classes is known as inheritance. Inheritance allows a new class, called a subclass, to inherit attributes and methods from an existing class, referred to as a base class. This mechanism promotes code reuse and establishes a hierarchical relationship between classes.

In this project, inheritance is utilized to create specialized versions of the Smiley class, such as Sad and Happy. The Sad class inherits from Smiley, allowing it to use and extend the functionality of the base class while modifying specific features, such as the appearance of the mouth and eyes. Similarly, Happy inherits from both Smiley and Blinkable, gaining additional functionality to implement blinking behavior. This structure enhances code organization, minimizes redundancy, and enables the addition of new features without altering existing code, promoting maintainability and scalability in the application.
>

### Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > difference between the Happy and Sad classes is their expressions. The Happy class incorporates functionality to blink, while the Sad class does not include any blinking behavior, resulting in a static appearance.
   >
2. What are the key similarities?
   > Both classes inherit from the Smiley class, allowing them to utilize the same pixel configuration and methods for displaying a face on the Sense HAT.
   >
3. What difference stands out the most to you and why?
   > the implementation of the blink method in the Happy class. This method not only enhances the visual expression of happiness but also introduces dynamic behavior that is absent in the Sad class.
   >
4. How does this difference affect the functionality of these classes
   > The Happy class can convey a more engaging and lively experience due to its blinking capability, while the Sad class remains static.
   >

### Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   >  Smiley, Happy, and Sad. All three classes rely on the methods provided by the SenseHat class to display their respective visual representations on the LED
   >
2. Which of these classes directly interact with the SenseHat functionalities?
   > The Smiley class works directly with SenseHat features, as it includes the main methods for displaying pixels (set_pixels) and controlling display settings (low_light). The Happy and Sad subclasses build on these functionalities, adding unique behaviors that correspond to their respective expressions. 
   >
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > Encapsulation is a key principle in object-oriented programming that involves limiting access to certain parts of an object to safeguard its internal state. In this project, the SenseHat class is encapsulated within the Smiley class, meaning that the details of how the LED matrix operates are concealed from the user. The user can interact with high-level methods like show and dim_display without needing to grasp the underlying mechanics of the SenseHat itself. This abstraction not only simplifies usage but also improves code maintainability, as developers can change the implementation of the SenseHat without impacting how the smiley faces are created or displayed. Consequently, the emphasis is placed on higher-level functionality rather than the intricacies of hardware interactions, resulting in a cleaner and more user-friendly interface.
   >

### Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> The code's author does not clearly state that every Smiley should have the ability to blink. The Blinkable class acts as an abstract base class (ABC) that outlines a blink method, indicating that blinking is an optional feature for smileys. Because the Sad class does not provide a blink method, it suggests that not all smileys are required to display this behavior.
>

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> The author understands that not all blinking smileys will blink identically. The blink method in the Happy class shows a particular way of blinking by switching the eyes between open and closed states with a delay. If the Sad class were to create its own blink method, it might exhibit a different behavior that aligns with its sad expression. This adaptability enables diverse implementations of the blinking behavior while still adhering to the shared interface established by the Blinkable class.
>

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Polymorphism is a programming concept that enables objects from different classes to be treated as instances of a common superclass. In the case of the Happy and Sad classes, polymorphism is showcased through the blink method defined in the Blinkable class. The Happy class has its own version of the blink method, while the Sad class currently does not implement this method. If the Sad class were to add a blink method, it could offer a unique blinking behavior that reflects its nature. This illustrates polymorphism, as both classes can be recognized as Blinkable types, yet their specific implementations of the blink method can differ.
>

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> The blink method is implemented using inheritance from the Blinkable abstract base class. The Happy class, which inherits from Blinkable, is required to define its own version of the blink method. This approach allows the Happy class to customize its blinking behavior while adhering to the interface set by Blinkable. This is crucial for polymorphism, as it permits various smiley classes to implement the blink method in unique ways, making them interchangeable in any context that uses the Blinkable interface. Therefore, inheritance supports polymorphism, enabling different behaviors to be executed depending on the specific subclass, which enhances the flexibility and reusability of the code.
>
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![img.png](img.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > The Sad smiley blink with a brief eye closure. I notice that the draw_eyes method needs to be adjusted for the Sad face when the eye position differs from the Happy face.

  ### If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > The Sad smiley should display its eyes in a “closed” state, hold it briefly, and then return to the “open” state.

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > Blinkable class achieves this by using the abstractmethod decorator from the abc module, ensuring that any subclass must implement the blink method. 

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > Abstraction is the process of creating a simplified model of a complex system by focusing on its key features and omitting irrelevant details. In this context, the Blinkable abstract base class offers a general framework for the blinking functionality that subclasses need to implement, without revealing the specifics of the blinking process. This approach enables various implementations while preserving a consistent interface.
  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > This flexibility arises from the concept of polymorphism, which allows different classes to implement methods that share the same name and signature, enabling interchangeable behavior. As long as the Sad Smiley's blink method replicates the functionality of the Happy Smiley's blink, it can be smoothly integrated into any situation that anticipates a blinking smiley, irrespective of the inheritance hierarchy. This ensures that both classes can offer distinct implementations of blinking while preserving a consistent interface for users of these classes.

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > In Python and many other dynamically typed languages, types are determined at runtime, which provides greater flexibility. This means that if an object has the necessary methods and behaviors, it can be used in place of another object with a similar interface, regardless of its actual class. On the other hand, statically typed languages like C# require explicit type definitions and often depend on inheritance hierarchies to enforce behavior. This can restrict flexibility because the compiler must know the exact type of an object at compile time, making it challenging to treat different types interchangeably unless they share a common base class or interface. This distinction allows dynamically typed languages to achieve more polymorphic behavior without the constraints of rigid class structures.

  ***

  ## Refactoring

  ### Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > in happy, sad, and smiley color is yellow
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > Variable type, it is stored as a variable
     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > The colour variable primarily used in the smiley, sad and happy classes. these classes relay on color variable to define the appearance of the smileys, such as the color of the face or other facial features.

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Apply the color we want in smiley file and chang the "self.YELLOW" to a color we desired.

  Here's a revised version of the "Flexible Colors – Step 1" section for the smiley project, incorporating your specifications for formatting and content updates:

  ### Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

![img_1.png](img_1.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
