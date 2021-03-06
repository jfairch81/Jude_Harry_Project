# Jude & Harry's Engineering 4 Project


#### Our Problem is finding the speed at which a Potato Cannon shoots a potato.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

### What is a Potato Cannon?

Potato Cannons are small scale projectile launchers. They function by utilizing Air Pressure to accelerate a projectile through a launch tube. There are different types of Potato Cannons, but we are building a **Combustion Driven Potato Cannon.**

> In this type of Potato Cannon, there is a combustion chamber and a launch tube. Before firing, propellant fills the combustion chamber, and is then ignited. For  > our project, we will be using a **Spark Plug** to ignite the propellant.



<img src="Media/Potato_Cannon.jpeg" width="300" height="200">


#### Propellents
Potato cannons can use a multitude of combustible fluids as "Fuel". 
This study does a great job of highlighting the benifits and drawbacks to very fuel. Although is seems that Acetylene is the clear winner, the drawbacks must be noted: the pressure caused by acetylene is immense and we are worried about it possibly breaking our PVC pipe.

##### Data
<img src="Media/Screenshot 2021-03-29 12.52.46 PM.png" width="400" height="200">        <img src="Media/Screenshot 2021-03-29 12.53.29 PM.png" width="300" height="200"> 
<img src="Media/Screenshot 2021-03-29 1.00.02 PM.png" width="400" height="150">

### For Reference
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Propellant  | Muzzle Velocity (MPH)
------------- | -------------
Acetylene  | 308.9 MPH
**Propane**  | **62.4 MPH**
Ethanol  | 74.5 MPH
Methanol  | 107.8 MPH
**Butane**  | **77.6 MPH**

Through research we've found that we can get Propane and Butane in spray cans, we may be able to access Ethanol or Methanol, but Acetylene is very expensive.
We will probably test both Propane and Butane on seperate launches after we get them.

**1 cc (Cubic Centimeter) = 1 mL (Milliliter)**

**1 mL of Butane = .599 g (grams)**                                                                                                                         
**1 mL of Propane = .583 g**

### Study
https://www.researchgate.net/publication/236627568_Studying_the_Internal_Ballistics_of_a_Combustion_Driven_Potato_Cannon_using_High-speed_Video

### Our Needs
We created a google doc outlining all the parts needed for this project. We included links for the parts we need to order aswell as a total estimated price. 

https://docs.google.com/document/d/1U25AbGJkagLkQlCdeDqdo1v5hj71Pqpnpsxfc6KjWwY/edit?usp=sharing
#### What we have as of now
Recently Harry went to Lowes and picked up the following parts :
- PVC cement and primer       <img src="Media/IMG_4184.jpg" width="200" height="200">   
- 2 inch PVC pipe             <img src="Media/IMG_4181.jpg" width="200" height="200">   
- Spark plug                  <img src="Media/IMG_4183.jpg" width="200" height="200">   
- 2-4 inch Coupler            <img src="Media/IMG_4186.jpg" width="200" height="200">   


### Potential Issues

Currently, We're three weeks out from the end of school. We are almost fully done with the building of the Potato Cannon, and we 3d printed a part so we can put the Pi in the Cannon. Our potato cannon currently is made out of 2 inch PVC on the barrel, and that might not be big enough to fit our Pi, as we 3d printed a spud and it fits but with the wiring it might not. We're contemplating whether moving to 3 inch PVC on the barrel will also be better.

Another one of our potential problems stems from the fact that since an explosion is happening in the cannon, the PVC may not withstand the blast. Whether that be heat, or when it is shot it might break. We plan on testing later this week to determine if this is fact or not.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

## Application

### Code

We plan on using a slightly modifiyed version of the I2C code to initially find the acceleration. It is gonna be a similar setup to the wiring also utilized in that assignment.

[Our Code:](https://github.com/jfairch81/Jude_Harry_Project/blob/main/Project_Code/projCode.py)

Wiring:   
          <img src="Media/Fritz1.png" width="200" height="100">  
### Potato Cannon

Here are a few pictures of our completed Potato Cannon before Harry and I launched it.

<img src="Media/IMG_0326.jpg" width="250" height="300">      <img src="Media/IMG_0325.jpg" width="200" height="300"> 

### Spud Design

Harry and I desgined our Spud through OnShape. We originally thought a 3 part design would be better, but found that that probably wouldn't work with the firing and if it disconnected and other problems. The second one is our actual design.

<img src="Media/OldSpud.png" width="400" height="300">   <img src="Media/Spud.png" width="400" height="300"> 

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

## Conclusion

On June Tenth Jude and I shot our potato cannon with a "test", 3D printed potato/spud without the raspberry pi, inside. We launched it from the top of a hill at Meade Park used a mix of propane and hair spray as a test before our actual shot. The spud shot relatively well but we ran into some issues with the durability of the spud. There were a few scorch marks and the top was damaged. We felt that it would be a waste school reasources to fire such a spud with a Raspberry Pi in side due to the lack of durability. If we had more time in the school year would would likely make the spud thicker, add more structuring to the inside, and run our own tests on various fuels.

<img src="Media/SpudP2.jpg" width="200" height="200">
