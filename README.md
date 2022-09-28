# enclipse
Enclipse is a cool opensource project to convert English natural language transcript into CLIPS Expert Systems syntax.
The idea is to utilize NLP techniques for command detection and feature extraction from the natural language input. 

e.g we may expect the following outputs given the corresponding inputs to the system:
```
$input[1]:
Cat template has properties of color, age, and name.
$output[1]:
(deftemplate cat
(slot color) (slot age) (slot name))
$input[2]: 
There exists a cat with the name Bob.
$output[2]:
(assert (cat (name “Bob”)))
$input[3]:
If there exists cat named Bob then there exists a cat named Tom.
$output[3]:
(defrule rule1
(cat (name “Bob”)) => (assert (cat (name “Tom”))))
```

# CLIPS
## What's [CLIPS](https://www.clipsrules.net/) 
**A Tool for Building Expert Systems**
Developed at NASA’s Johnson Space Center from 1985 to 1996, the C Language Integrated Production System (CLIPS) is a rule‑based programming language useful for creating expert systems and other programs where a heuristic solution is easier to implement and maintain than an algorithmic solution. 
## Why CLIPS?
we chose CLIPS language since the syntax and the prinicples are pretty simple and senarios are pretty basic. Here is an [intro to CLIPS syntax and semantics](https://www.clipsrules.net/documentation/v640/bpg640.pdf). take a look! it's fun! 
# Contribution
For contribution you can simply clone the repo, check the issues section and create a branch with the correspondant name in the issue. finally you can make a pull-request to the origin/develop branch. 
 
