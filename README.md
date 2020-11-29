# Numerical Methods &amp; Optimization Algorithms

The idea of this implementation was to understand numerical methods and optimization algorithms better through their implementation in Python. 

All of the UI/Server is handled in Shiny<b>(R)</b>, and the back-end runs on a Python script. 

In order to use the application, you can clone this repo and then you can run the app through either of the .R files. If you have shiny installed, you should be able to see the button to run the shiny app. 

![Run the app](https://i.imgur.com/31Kydp0.png)



<b>Here's the list of the methods/algorithms available in the app:</b>

<ul>
  <li>Finite Differences</li>
  <li>Trapezoidal Rule</li>
  <li>Incremental Search Method</li>
  <li>Bisection Method</li>
  <li>Newton-Raphson</li>
  <li>FONC SONC SOSC Evaluator</li>
  <li>Steepest Descent</li> 
</ul>

Feel free to use this and modify or improve them in any way you'd like. There are still some particular constraints in relation to how you input the functions/values that can be improved.

Here's an example of how you can use the Steepest Descent algorithm. You just need to enter the function, the two initial points for the search, and a value for epsilon. 

![Steepest Descent Example](https://i.imgur.com/53Faoob.png)

And as you can see you'll get the exact points at which the function is minimized near that interval and the value evaluated at the minimum.

---
### Authors
* Omar Eduardo Martinez
* Joaquin Orantes
